from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from enum import Enum
from collections import defaultdict


class Command:
    def __init__(self, line):
        tmp = line.split()[1:]
        self.command = tmp[0]
        if len(tmp) > 1:
            self.option = tmp[1]


class Output:
    def __init__(self):
        self.lines = []
        self.files = []

    def add(self, line):
        self.lines.append(line)

    def parse(self):
        for line in self.lines:
            tokens = line.split()
            if tokens[0] == 'dir':
                self.files.append(Directory(tokens[1]))
            else:
                self.files.append(DataFile(name=tokens[1], size=tokens[0]))
        return self.files


class FileTypes(Enum):
    FOLDER = 'folder'
    FILE = 'file'


class File:
    def __init__(self, file_type: FileTypes, name: str):
        self.type = file_type
        self.name = name


class Directory(File):
    def __init__(self, name):
        super().__init__(FileTypes.FOLDER, name)

    def __str__(self):
        return f'dir {self.name}'


class DataFile(File):
    def __init__(self, name, size):
        super().__init__(FileTypes.FILE, name)
        self.size = size

    def __str__(self):
        return f'{self.size} {self.name}'


class Program:
    def __init__(self, disk):
        self.disk = disk

    def execute(self, lines):
        output = Output()
        for line in lines:
            if line.startswith('$'):
                files = output.parse()
                self._process_files(files)
                self._process_command(Command(line))
                output = Output()
            else:
                output.add(line)
        self._process_files(output.parse())

    def _process_files(self, files):
        for file in files:
            if file.type == FileTypes.FILE:
                print('adding', file.name, 'to', self.current_folder)
                self.disk.add_file(file)

    def _process_command(self, command: Command):
        if command.command == 'cd':
            if command.option == '..':
                print('changing folder to', self.disk.current_folder.parent)
                self.disk.navigate_up()
            else:
                print('changing directory to', command.option)
                self.disk.navigate_to(Directory(command.option))
                self.current_folder = command.option


class Disk:
    def __init__(self, total_space):
        self.root = None
        self.size = defaultdict(int)
        self.current_folder = None
        self.number = 0
        self.total_space = total_space

    def navigate_to(self, _dir: Directory):
        if self.root is None:
            self._create_root()
        else:
            parent = self.current_folder
            node = Node(f'{_dir.name}_{str(self.number)}', parent)
            self.current_folder = node
            self.number += 1

    def _create_root(self):
        print('creating root')
        self.root = Node('root')
        self.current_folder = self.root

    def add_file(self, _file: DataFile):
        parent = self.current_folder
        while parent is not None:
            self.size[parent.name] += int(_file.size)
            parent = parent.parent

    def navigate_up(self):
        self.current_folder = self.current_folder.parent

    def sum_of_folder_size_under(self, threshold):
        _sum = 0
        for (folder, size) in self.size.items():
            if size < threshold:
                _sum += size
        return _sum

    def folder_to_delete(self, free_space_needed):
        bytes_to_delete = free_space_needed - self.free_space()
        big_enough_folders = []
        for (folder, folder_size) in self.size.items():
            diff = bytes_to_delete - folder_size
            if diff <= 0:
                big_enough_folders.append((abs(diff), folder_size))
        big_enough_folders.sort(key=lambda x: x[0])
        return big_enough_folders[0][1]

    def free_space(self):
        return self.total_space - self.size['root']


def execute():
    needed_space = 30000000
    disk = Disk(70000000)
    program = Program(disk)
    with open('data/7.txt') as file:
        program.execute(file.readlines())
    print('sum of folder size for folders under', 100000, ':', disk.sum_of_folder_size_under(100000))
    print('size of folder to delete:', disk.folder_to_delete(needed_space))


if __name__ == '__main__':
    execute()

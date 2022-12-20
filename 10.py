from enum import Enum


class Instruction:
    def __init__(self, name):
        self.name = name


class Noop(Instruction):
    def __init__(self):
        super().__init__('noop')


class Addx(Instruction):
    def __init__(self, value):
        super().__init__('addx')
        self.value = value


class Monitor:
    def __init__(self):
        self.pixels = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        self.pixel = 0
        self.row_number = 0

    def tick(self, position):
        row = self.pixels[self.row_number]
        sprite_position = [position - 1, position, position + 1]
        if self.pixel in sprite_position:
            char = '# '
        else:
            char = ". "
        print('row', self.row_number, 'pixel number', self.pixel, 'char', char, 'sprite position', sprite_position)
        row.append(char)
        self.pixel += 1
        if self.pixel == 40:
            self.pixel = 0
            self.row_number += 1
            if self.row_number == 6:
                self.row_number = 0
class CPU:
    def __init__(self):
        self.register = 1
        self.operation_countdown = 0
        self.instruction = None

    def tick(self):
        self.operation_countdown -= 1
        if self.operation_countdown == 0:
            if type(self.instruction) is Addx:
                self.register += self.instruction.value

    def add_instruction(self, operation):
        self.instruction = operation
        if type(operation) is Addx:
            self.operation_countdown = 2
        else:
            self.operation_countdown = 1


class Computer:
    cpu = CPU()
    monitor = Monitor()
    cycle = 1
    stored_values = []

    def instruction(self, operation):
        self.cpu.add_instruction(operation)
        self.tick()
        if type(operation) is Addx:
            self.tick()

    def tick(self):
        if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
            self.stored_values.append(self.cpu.register * self.cycle)
        self.monitor.tick(self.cpu.register)
        self.cpu.tick()
        self.cycle += 1


def execute():
    computer = Computer()
    with open('data/10.txt') as file:
        for line in file:
            tmp = line.strip().split()
            if line.startswith('addx'):
                computer.instruction(Addx(int(tmp[1])))
            else:
                computer.instruction(Noop())
        print(computer.stored_values)
        print(sum(computer.stored_values))
        for row_number in sorted(computer.monitor.pixels.keys()):
            for pixel in computer.monitor.pixels[row_number]:
                print(pixel, end='')
            print()


if __name__ == '__main__':
    execute()

from collections import defaultdict


class Command:
    def __init__(self, line):
        tmp = list(map(lambda x: x.strip(), line.split(' ')))
        self.action = tmp[0]
        self.amount = int(tmp[1])
        self.from_stack = int(tmp[3])
        self.to_stack = int(tmp[5])


class Stack:
    def __init__(self):
        self.boxes = []

    def reverse(self):
        self.boxes.reverse()

    def add(self, box):
        self.boxes.append(box)

    def add_boxes(self, boxes):
        self.boxes.extend(boxes)

    def get(self, amount=None):
        if amount is None:
            return self.boxes.pop()
        else:
            to_return = self.boxes[-amount:]
            for index in range(amount):
                self.boxes.pop()
            return to_return


class Stacks:
    def __init__(self):
        self.stacks = defaultdict(Stack)

    def flip_stacks(self):
        for (stack_number, stack) in self.stacks.items():
            self.stacks[stack_number].reverse()

    def add(self, box, stack):
        self.stacks[stack].add(box)

    def move(self, command):
        for box in range(command.amount):
            box = self.stacks[command.from_stack].get()
            self.stacks[command.to_stack].add(box)

    def move_2(self, command):
        boxes_to_move = self.stacks[command.from_stack].get(command.amount)
        self.stacks[command.to_stack].add_boxes(boxes_to_move)

    def get_top_boxes(self):
        sorted_indexes = sorted(self.stacks.keys())
        top_boxes = ''
        for stack_number in sorted_indexes:
            box = str(self.stacks[stack_number].get())
            top_boxes += box
        return top_boxes


def parse_stacks(line, stacks):
    stack_number = 1
    while len(line) > 2:
        token = line[0:4]
        if len(token.strip()) > 0:
            box = token[1]
            stacks.add(box, stack_number)
        line = line[4:]
        stack_number += 1


def execute():
    with open('data/5.txt') as file:
        stacks = Stacks()
        parsing_stacks = True
        line_number = 0
        while parsing_stacks:
            line = file.readline()
            if len(line.strip()) != 0 and not line.startswith(' 1'):
                parse_stacks(line, stacks)
                line_number += 1
                print('parsing line', line_number)
            else:
                parsing_stacks = False
        stacks.flip_stacks()
        file.readline()  # Reading the numbers
        for index, line in enumerate(file):
            print('executing command on line:', index + 1)
            command = Command(line)
            stacks.move(command)
        print(stacks.get_top_boxes())


def execute2():
    with open('data/5.txt') as file:
        stacks = Stacks()
        parsing_stacks = True
        line_number = 0
        while parsing_stacks:
            line = file.readline()
            if len(line.strip()) != 0 and not line.startswith(' 1'):
                parse_stacks(line, stacks)
                line_number += 1
                print('parsing line', line_number)
            else:
                parsing_stacks = False
        stacks.flip_stacks()
        file.readline()  # Reading the numbers
        for index, line in enumerate(file):
            print('executing command on line:', index + 1)
            command = Command(line)
            stacks.move_2(command)
        print(stacks.get_top_boxes())


if __name__ == '__main__':
    # execute()
    execute2()

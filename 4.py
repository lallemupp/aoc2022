from util import util


class Assignment:
    def __init__(self, index, first, second):
        self.index = index
        self.first = list(range(int(first.split('-')[0]), int(first.split('-')[1]) + 1))
        self.second = list(range(int(second.split('-')[0]), int(second.split('-')[1]) + 1))

    def check_contains(self):
        longest, shortest = util.get_longest(self.first, self.second)
        contains = True
        for number in shortest:
            if number not in longest:
                contains = False
                break
        return contains

    def overlaps(self):
        longest, shortest = util.get_longest(self.first, self.second)
        for number in shortest:
            if number in longest:
                return True
        return False

    def __str__(self):
        return f'assignment {self.index}:\nfirst: {self.first}\nsecond: {self.second}'


def execute():
    with open('data/4.txt') as file:
        total = 0
        for index, line in enumerate(file):
            split_line = line.split(',')
            assignment = Assignment(index + 1, split_line[0], split_line[1])
            if assignment.check_contains():
                print(assignment)
                total += 1
            print(total)


def execute2():
    with open('data/4.txt') as file:
        total = 0
        for index, line in enumerate(file):
            split_line = line.split(',')
            assignment = Assignment(index + 1, split_line[0], split_line[1])
            if assignment.overlaps():
                print(assignment)
                total += 1
        print(total)


if __name__ == '__main__':
    execute()
    execute2()

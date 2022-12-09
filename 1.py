from util.util import MaxList


class Elf:
    def __init__(self, number, calories=0):
        self.number = number
        self.calories = calories

    def add(self, calories):
        self.calories += calories

    def __str__(self):
        return f'{self.number}: {self.calories}'


class Inventory:
    def __init__(self):
        self.inventory = []

    def add(self, an_elf):
        self.inventory.append(an_elf)

    def highest_calories(self):
        max_elf = Elf(-1, -1)
        for _elf in self.inventory:
            if _elf.calories > max_elf.calories:
                max_elf = _elf
        return max_elf

    def top_three(self):
        top_three_elfs = MaxList(size=3)
        for _elf in self.inventory:
            top_three_elfs.add_if_higher(value=_elf.calories, data=_elf)
        return top_three_elfs.max_it.values()


def parse(file):
    inventory = Inventory()
    with open(file) as file:
        elf_number = 1
        _elf = Elf(elf_number)
        for line in file:
            if len(line.strip()) == 0:
                inventory.add(_elf)
                elf_number += 1
                _elf = Elf(elf_number)
            else:
                _elf.add(calories=int(line.strip()))
    return inventory


def execute():
    elfs = []
    with open('data/1.txt') as file:
        lines = file.readlines()
        elf = 0
        for line in lines:
            if line.isspace():
                elfs.append(elf)
                elf = 0
            else:
                elf += int(line)
    elfs = sorted(elfs, reverse=True)
    print('max', elfs[0], 'top three', sum(elfs[0:3]))


if __name__ == '__main__':
    elfs = parse('data/1.txt')
    top_elf = elfs.highest_calories()
    print('top elf with number', top_elf.number, 'carries', top_elf.calories, 'calories')
    top_three = (elfs.top_three())
    total = 0
    for elf in top_three:
        total += elf.calories
    print('total of top three elfs:', total, 'calories')
    execute()

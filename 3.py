import collections
import string


def item_type_to_prio(item_type):
    order = string.ascii_lowercase.index(item_type.lower()) + 1
    if item_type.isupper():
        return order + 26
    else:
        return order


class Group:
    def __init__(self):
        self.rucksacks = []

    def add_to_group(self, rucksack):
        self.rucksacks.append(rucksack)

    def find_badge_prio_number(self):
        item_types = collections.defaultdict(int)
        for rucksack in self.rucksacks:
            added = []
            for item_type in rucksack.pack_string:
                if item_type not in added:
                    item_types[item_type] += 1
                    added.append(item_type)
                    if item_types[item_type] == 3:
                        return item_type_to_prio(item_type)
        exit(22)


class Rucksack:
    def __init__(self, pack_string):
        self.pack_string = pack_string
        self.compartment_1 = pack_string[len(pack_string)//2:]
        self.compartment_2 = pack_string[:len(pack_string)//2]

    def duplicate_prio(self):
        for item_type in self.compartment_1:
            if item_type in self.compartment_2:
                order = string.ascii_lowercase.index(item_type.lower()) + 1
                if item_type.isupper():
                    return order + 26
                else:
                    return order


def execute():
    with open('data/3.txt') as file:
        total_prio = 0
        for line in file:
            rucksack = Rucksack(line.strip())
            total_prio += rucksack.duplicate_prio()
        print(total_prio)


def execute_part_2():
    with open('data/3.txt') as file:
        total_prio = 0
        group = Group()
        for line in file:
            rucksack = Rucksack(line)
            group.add_to_group(rucksack)
            if len(group.rucksacks) == 3:
                total_prio += group.find_badge_prio_number()
                group = Group()
        print(total_prio)


if __name__ == '__main__':
    execute()
    execute_part_2()

from util.util import add, multiply, mod


class Action:
    def __init__(self, item, monkey):
        self.item = item
        self.monkey = monkey

    def __str__(self):
        return f'{self.item} to monkey {self.monkey}'

class Monkey:
    def __init__(self, lines: list):
        self.number = int(lines[0].split()[1][0])
        self.items = [int(item.strip(',')) for item in lines[1].split()[2:]]
        operator = add if [lines[2].split()[5]] == '+' else multiply
        self.operation = lambda x: operator(x, int(lines[2].split()[5]))
        self.test = int(lines[3].split()[3])
        self.positive = int(lines[4].split()[5])
        self.negative = int(lines[5].split()[5])
        self.inspected_items = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect_items(self):
        actions = []
        for item in self.items:
            new_level = self.operation(item)
            new_level = Monkey.get_bored(new_level)
            monkey = self.positive if mod(new_level, self.test) else self.negative
            actions.append(Action(new_level, monkey))
            self.items.remove(item)
            self.inspected_items += 1
        return actions

    @staticmethod
    def get_bored(worry_level):
        return int(worry_level / 3)

    def __str__(self):
        return f'{[item for item in self.items]}'


def execute():
    with open('data/test.txt') as file:
        monkeys = {}
        for line in file:
            if len(line.strip()) == 0:
                next(file)
            lines = [next(file) for _ in range(5)]
            lines.insert(0, line)
            monkey = Monkey(lines)
            monkeys[monkey.number] = monkey
        for monkey in monkeys.values():
            actions = monkey.inspect_items()
            for action in actions:
                monkeys[action.monkey].add_item(action.item)
        for monkey in monkeys.values():
            print(monkey)


if __name__ == '__main__':
    execute()
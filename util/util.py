class CircularList:
    def __init__(self):
        self.values = [0, 0, 0]
        self.inserts = 0

    def add(self, to_add):
        self.values.append(to_add)
        self.values.pop(0)
        if self.inserts < 3:
            self.inserts += 1

    def total(self):
        return sum(self.values)

    def full(self):
        return self.inserts == 3


class MaxList:
    def __init__(self, size):
        self.added = 0
        self.size = size
        self.max_it = {}

    def add_if_higher(self, value, data):
        if self.added < self.size:
            self.max_it[value] = data
            self.added += 1
        elif value > self.lowest_value():
            self.max_it.pop(self.lowest_value())
            self.max_it[value] = data

    def lowest_value(self):
        return min(self.max_it.keys())


def get_longest(first, second):
    if len(first) > len(second):
        longest = first
        shortest = second
    else:
        longest = second
        shortest = first
    return longest, shortest

from collections import defaultdict
from util.util import transpose
import numpy as np


def is_visible(first, second, tree):
    return len(first) == 0 or len(second) == 0 or \
        (max(first, key=lambda t: t.height).height < tree.height or
         max(second, key=lambda t: t.height).height < tree.height)

class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = True

    def __str__(self):
        return f'({self.height}, {self.visible})'


class Forest:
    def __init__(self):
        self.matrix = None

    def _heights(self, row):
        return list(map(lambda tree: tree.height, self.matrix[row]))
    def add_row(self, row):
        _temp = [Tree(x) for x in row]
        if self.matrix is None:
            self.matrix = [_temp]
        else:
            self.matrix = np.append(self.matrix, [_temp], axis=0)

    def check_tree_visibility(self):
        print(self.matrix)
        for row in self.matrix:
            for index, tree in enumerate(row):
                first = row[0: index]
                second = row[index + 1:]
                tree.visible = is_visible(first, second, tree)
        for column_number in range(len(self.matrix[0])):
            column = self.matrix[:column_number]
            for tree in column:
                first = column[0: index]
                second = column[index + 1:]
                tree.visible = is_visible(first, second, tree)

    def number_of_visible_trees(self):
        _sum = 0
        for row in self.matrix:
            _sum += len(list(filter(lambda tree: tree.visible, row)))
        return _sum

    def __str__(self):
        as_string = ''
        for row in self.matrix:
            for tree in row:
                as_string += f' {tree}'
            as_string += '\n'
        return as_string

def execute():
    forest = Forest()
    with open('data/test.txt') as file:
        for line in file:
            forest.add_row(line.strip())
    forest.check_tree_visibility()
    print(forest)
    print(forest.number_of_visible_trees())


if __name__ == '__main__':
    execute()

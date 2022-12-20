from collections import defaultdict
from util.util import transpose
import numpy as np


def is_visible(before, after, tree):
    tree_on_edge = len(before) == 0 or len(after) == 0
    if tree_on_edge:
        return True
    blocked_before = max(before, key=lambda t: t.height).height < tree.height
    blocked_after = max(after, key=lambda t: t.height).height < tree.height
    return tree_on_edge or blocked_before or blocked_after

def view_distance(before, after, tree):
    distance_before = check_for_higher_trees(np.flip(before), tree.height)
    distance_after = check_for_higher_trees(after, tree.height)
    return distance_after, distance_before

def check_for_higher_trees(_list, height):
    higher_trees_before = []
    for tree in _list:
        higher_trees_before.append(tree)
        if tree.height >= height:
            return len(higher_trees_before)
    return len(_list)

class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = True
        self.view_distance = []

    def __str__(self):
        return f'({self.height}, {self.visible})'


class Forest:
    def __init__(self):
        self.trees = None

    def _heights(self, row):
        return list(map(lambda tree: tree.height, self.trees[row]))
    def add_row(self, row):
        _temp = [Tree(x) for x in row]
        if self.trees is None:
            self.trees = [_temp]
        else:
            self.trees = np.append(self.trees, [_temp], axis=0)

    def check_tree_visibility(self):
        for row in self.trees:
            for index, tree in enumerate(row):
                before = row[0: index]
                after = row[index + 1:]
                tree.visible = is_visible(before, after, tree)
        for column in self.trees.T:
            for index, tree in enumerate(column):
                if not tree.visible:
                    before = column[0: index]
                    after = column[index + 1:]
                    visible = is_visible(before, after, tree)
                    tree.visible = visible

    def max_scenic_score(self):
        for row in self.trees:
            for index, tree in enumerate(row):
                before = row[0: index]
                after = row[index + 1:]
                left, right = view_distance(before, after, tree)
                tree.view_distance.extend([left, right])
        for column in self.trees.T:
            for index, tree in enumerate(column):
                before = column[0: index]
                after = column[index + 1:]
                up, down = view_distance(before, after, tree)
                tree.view_distance.extend([up, down])
        max_scenic_score = 0
        for tree in np.nditer(self.trees, flags=["refs_ok"]):
            item = tree.item(0)
            max_scenic_score = max(max_scenic_score, np.prod(item.view_distance))
        return max_scenic_score


    def number_of_visible_trees(self):
        _sum = 0
        for row in self.trees:
            _sum += len(list(filter(lambda tree: tree.visible, row)))
        return _sum

    def __str__(self):
        as_string = ''
        for row in self.trees:
            for tree in row:
                as_string += f' {tree}'
            as_string += '\n'
        return as_string

def execute():
    forest = Forest()
    with open('data/8.txt') as file:
        for line in file:
            forest.add_row(line.strip())
    forest.check_tree_visibility()
    print(forest)
    print('max number of visible trees:', forest.number_of_visible_trees())
    print('max scenic score', forest.max_scenic_score())


if __name__ == '__main__':
    execute()

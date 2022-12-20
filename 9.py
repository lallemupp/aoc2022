from enum import Enum
from math import copysign
from util.util import take_first, take_second


def moving_distance(distance):
    value = distance
    if abs(distance) > 0:
        value = copysign(1, value)
    return value


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_position(self, x, y):
        self.x += x
        self.y += y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return self.x, self.y

    def distance_to(self, other):
        delta = self.delta_to(other)
        return max(abs(delta[0]), abs(delta[1]))

    def delta_to(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        return delta_x, delta_y

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'

    @staticmethod
    def from_string(string):
        if string == 'U':
            return Direction.UP
        if string == 'D':
            return Direction.DOWN
        if string == 'L':
            return Direction.LEFT
        if string == 'R':
            return Direction.RIGHT


class Movement:
    def __init__(self, line):
        temp = line.split()
        self.direction = Direction.from_string(temp[0])
        self.steps = int(temp[1])


class Rope:
    def __init__(self, number_of_knots):
        self.knots = [Position(0, 0) for x in range(number_of_knots)]
        self.visited_tail_positions = set()
        self.visited_tail_positions.add((0, 0))

    def move_head(self, movement: Movement):
        for i in range(movement.steps):
            x = y = 0
            if movement.direction is Direction.UP:
                y = 1
            elif movement.direction is Direction.DOWN:
                y = -1
            elif movement.direction is Direction.LEFT:
                x = -1
            elif movement.direction is Direction.RIGHT:
                x = 1
            self.knots[0].update_position(x, y)
            for j in range(1, len(self.knots)):
                tail = self.knots[j]
                head = self.knots[j - 1]
                if tail.distance_to(head) > 1:
                    self._move_tail(tail, head, movement.direction, j, j == len(self.knots) - 1)

    def _move_tail(self, tail, head, direction, knot_number, last_knot):
        while tail.distance_to(head) > 1:
            x = y = 0
            delta = head.delta_to(tail)
            tail.update_position(moving_distance(delta[0]), moving_distance(delta[1]))
            if last_knot:
                self.visited_tail_positions.add(tail.as_tuple())

    def print_visited(self):
        max_x = take_first(max(self.visited_tail_positions, key=take_first)) + 10
        max_y = take_second(max(self.visited_tail_positions, key=take_second)) + 10
        min_x = take_first(min(self.visited_tail_positions, key=take_first)) - 10
        min_y = take_second(min(self.visited_tail_positions, key=take_second)) - 10
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if (x, y) == (0, 0):
                    print('s ', end='')
                elif (x, y) in self.visited_tail_positions:
                    print('# ', end='')
                else:
                    print('. ', end='')
            print()

    def print_knots(self, _grid_size):
        max_x = max_y = int(_grid_size / 2)
        min_x = min_y = -int(_grid_size / 2)
        for y in reversed(range(min_y, max_y)):
            for x in range(min_x, max_x):
                pos = Position(x, y)
                if (x, y) == (0, 0):
                    print('s ', end='')
                elif pos in self.knots:
                    print(f'{self.knots.index(pos)} ', end='')
                else:
                    print('. ', end='')
            print()
        print()


def execute(number_of_knots):
    bridge = Rope(number_of_knots)
    with open('data/9.txt') as file:
        for line in file:
            movement = Movement(line.strip())
            bridge.move_head(movement)
    print(len(bridge.visited_tail_positions))


if __name__ == '__main__':
    execute(2)
    execute(10)

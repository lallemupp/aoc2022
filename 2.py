translation_map = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

class Game:
    # [ROCK, PAPER, SCISSORS]
    them_code = ['A', 'B', 'C']
    me_code = ['X', 'Y', 'Z']

    def __init__(self, line):
        choices = line.split()
        self.them = self.them_code.index(choices[0]) + 1
        self.me = self.me_code.index(choices[1]) + 1

    def outcome(self):
        print('them:', translation_map[self.them], '\nme:  ', translation_map[self.me])
        weight = self.me - self.them
        if weight == 1 or (weight == -2 and self.me == 1):
            points = self.me + 6
            outcome = 'win'
        elif weight == 0:
            points = self.me + 3
            outcome = 'draw'
        else:
            points = self.me
            outcome = 'loss'
        print('outcome', outcome, '\npoints:', points, '\n')
        return points


def execute():
    with open('data/2.txt') as file:
        total = 0
        for line in file:
            game = Game(line)
            total += game.outcome()
    print('total points', total)


def execute_test(data):
    total = 0
    for line in data:
        game = Game(line)
        outcome = game.outcome()
        print(outcome)
        total += outcome
    print(total)


if __name__ == '__main__':
    execute()
    # execute_test(['A Y', 'B X', 'C Z'])

translation_map = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
result_translation_map = {1: 'Lose', 2: 'Draw', 3: 'Win'}


class Game:
    # [ROCK, PAPER, SCISSORS]
    them_code = ['A', 'B', 'C']
    me_code = ['X', 'Y', 'Z']
    result_code = ['X', 'Y', 'Z']

    def __init__(self, line):
        choices = line.split()
        self.them = self.them_code.index(choices[0]) + 1
        self.result = self.result_code.index(choices[1]) + 1
        self.me = self.get_correct_choice()

    def get_correct_choice(self):
        if self.result == 2:
            choice = self.them
        elif self.result == 3:
            choice = self.them + 1
            if choice > 3:
                choice = 1
        else:
            choice = self.them - 1
            if choice < 1:
                choice = 3
        if choice not in [1, 2, 3]:
            print('choice out of bounds')
            print('them:', self.them, 'result:', self.result, 'me:', choice)
            exit(-1)
        return choice

    def outcome(self):
        print('them:', translation_map[self.them], '\nme:  ', translation_map[self.me])
        weight = self.me - self.them
        if weight == 1 or (weight == -2 and self.me == 1):
            points = self.me + 6
            outcome = 3
        elif weight == 0:
            points = self.me + 3
            outcome = 2
        else:
            points = self.me
            outcome = 1
        if self.result != outcome:
            print('ERROR!!!!')
            print('them', self.them, 'me', self.me, 'Planned outcome:',
                  result_translation_map[self.result], '\nOutcome        :', result_translation_map[outcome])
            exit(10)
        print('Planned outcome:', result_translation_map[self.result], '\nOutcome        :',
              result_translation_map[outcome], '\npoints:', points, '\n')
        return points


def execute():
    with open('data/2.txt') as file:
        total = 0
        for line in file:
            game = Game(line)
            total += game.outcome()
    print('total points', total)


if __name__ == '__main__':
    execute()

class Sequence:
    def __init__(self, char_sequence, token_length):
        self.index = 0
        self.token_length = token_length
        self.sequence = char_sequence

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index + self.token_length > len(self.sequence):
            raise StopIteration
        token = self.sequence[self.index:self.index + self.token_length]
        self.index += 1
        return token


def execute():
    with open('data/6.txt') as file:
        sequence = Sequence(file.readline(), 4)
        for index, token in enumerate(sequence):
            if len(token) == len(set(token)):
                print(token, 'found after', index + sequence.token_length, 'chars')
                return
        exit(12)


def execute2():
    with open('data/6.txt') as file:
        sequence = Sequence(file.readline(), 14)
        for index, token in enumerate(sequence):
            if len(token) == len(set(token)):
                print(token, 'found after', index + sequence.token_length, 'chars')
                return
        exit(12)


if __name__ == '__main__':
    execute()
    execute2()


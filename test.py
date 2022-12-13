import numpy as np

if __name__ == '__main__':
    apa = [[1, 2, 3]]
    apa = np.append(apa, [[1, 2, 3]], axis=0)
    apa = np.append(apa, [[4,5,6]], axis=0)
    print(apa)
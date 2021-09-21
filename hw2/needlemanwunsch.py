import numpy as np


class NeedlemanWunsch:
    def __init__(self, s, t, delta=lambda x, y: 2 if x == y else -1):
        self.s = s
        self.t = t
        self.delta = delta
        self.n = len(s)
        self.m = len(t)
        self.V = np.full(shape=(self.n + 1, self.m + 1), fill_value=None, dtype=object)
        for i in range(self.n + 1):
            for j in range(self.m + 1):
                self.V[i, j] = Cell()

    def calc(self):
        # Filling base conditions
        for i in range(self.n + 1):
            self.V[i, 0] = -i
        for j in range(self.m + 1):
            self.V[0, j] = -j

        # Filling rest of the table row by row
        for i in range(1, self.n + 1):
            # print(self.s[i - 1])
            for j in range(1, self.m + 1):
                self.V[i, j] = max(self.V[i - 1, j - 1] + self.delta(self.s[i - 1], self.t[j - 1]),
                                   self.V[i - 1, j] - 1, self.V[i, j - 1] - 1)

    def getOptScore(self):
        return self.V[-1, -1]

    def print(self):
        for i in range(self.n + 1):
            for j in range(self.m + 1):
                print(self.V[i, j].val, end=' ')
            print("\n")


class Cell:

    def __init__(self):
        self.val = 0
        self.up = False
        self.left = False
        self.diag = False

    def setVal(self, val):
        self.val = val

    def print(self):
        print(self.val)


def main():
    print("Running Needleman-Wunsch Algorithm")
    nw = NeedlemanWunsch("adsdf", "sdjfhsdf", lambda x, y: 2)
    nw.print()
    print(nw.delta(3, 6))

    nw2 = NeedlemanWunsch("ACAATCC", "AGCATGC")
    nw2.print()
    print(nw2.delta(1, 2))
    nw2.V[3, 2].setVal(8)
    nw2.calc()
    print(nw2.V)


if __name__ == '__main__':
    main()

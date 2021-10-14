import numpy as np


def main():
    s = "banana$"
    sa = SA(s)
    print(sa.sa)

    temp = [s[sa.sa[i] - 1] if sa.sa[i] != 0 else s[-1] for i in range(len(sa.sa))]
    print(temp)

    bw = sa.getBW()
    print(bw)

    print(sa.alphabet())
    print(sa.getCount())

    print(sa.occds)
    pass


class SA():
    def __init__(self, S):
        self.s = S
        self.sa = self.sort()
        self.bw = self.getBW()
        self.C = self.getCount()
        self.occds = self.occ()

    def sort(self):
        return [rank for suffix, rank in sorted((self.s[i:], i) for i in range(len(self.s)))]

    def getBW(self):
        return [self.s[self.sa[i] - 1] if self.sa[i] != 0 else self.s[-1] for i in range(len(self.sa))]
        pass

    def alphabet(self):
        return sorted(list(set(self.s)))

    def getCount(self):
        alphabet = self.alphabet()
        count = dict.fromkeys(self.alphabet(), 0)
        for c in self.s:
            count[c] = count[c] + 1

        C = dict.fromkeys(alphabet, 0)
        prev = 0
        prevC = None
        for c in alphabet:
            if prevC == None:
                C[c] = prev
                prev = count[c]
                prevC = c
            else:
                C[c] = prev
                prev = prev + count[c]
                prevC = c

        return C

    def occ(self):
        occds = dict.fromkeys(self.alphabet(), None)
        for k in occds.keys():
            occds[k] = np.full(len(self.bw), 0)
        for a in self.alphabet():
            prev = 0
            for i in range(len(self.bw)):
                if self.bw[i] == a:
                    occds[a][i] = prev + 1
                    prev = prev + 1
                else:
                    occds[a][i] = prev
        return occds


if __name__ == '__main__':
    main()

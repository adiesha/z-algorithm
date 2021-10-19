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

    def getOccds(self, x, i):
        if i < 0:
            return 0
        else:
            return self.occds[x][i]

    def printoccds(self):
        for k, v in self.occds.items():
            print(k + " : " + str(v))

    def binarysearchsa(self, pattern):
        l = 0
        r = len(self.sa) - 1
        while (l <= r):
            m = int((l + r) / 2)
            prefix = self.findprefix(self.s[self.sa[m]:], pattern)
            if len(prefix) == len(pattern):
                return True, self.s[self.sa[m]:]
            elif self.s[self.sa[m]] > pattern:
                r = m - 1
            else:
                l = m + 1
        if l > r:
            return False, None

    def findprefix(self, s, pattern):
        l = min(len(s), len(pattern))
        count = 0
        for i in range(l):
            if pattern[i] == s[i]:
                count = count + 1
            else:
                break
        return pattern[0:count]

    def backwardsearch(self, pattern):
        st = 0
        ed = len(self.s) - 1
        i = len(pattern) - 1
        while st <= ed and i >= 0:
            x = pattern[i]
            st = self.C[x] + self.getOccds(x, st - 1)
            ed = self.C[x] + self.getOccds(x, ed) - 1
            i -= 1
        if st <= ed:
            return True, (st, ed)
        else:
            return False, None


if __name__ == '__main__':
    main()

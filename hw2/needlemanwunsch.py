import networkx as nx
import numpy as np


class NeedlemanWunsch:
    def __init__(self, s, t, delta=lambda x, y: 2 if x == y else -1):
        self.s = s
        self.t = t
        self.delta = delta
        self.n = len(s)
        self.m = len(t)
        self.V = np.full(shape=(self.n + 1, self.m + 1), fill_value=0)
        self.G = nx.DiGraph()
        self.G.add_nodes_from(range((self.m + 1) * (self.n + 1)))

    def calc(self):
        # Filling base conditions
        for i in range(self.n + 1):
            self.V[i, 0] = -i
            if i != 0:
                self.G.add_edge(self.getNodeIDfromIndex(i, 0), self.getUpNodeId(i, 0))
        for j in range(self.m + 1):
            self.V[0, j] = -j
            if j != 0:
                self.G.add_edge(self.getNodeIDfromIndex(0, j), self.getLeftNodeId(0, j))

        # Filling rest of the table row by row
        for i in range(1, self.n + 1):
            # print(self.s[i - 1])
            for j in range(1, self.m + 1):
                diag = self.V[i - 1, j - 1] + self.delta(self.s[i - 1], self.t[j - 1])
                up = self.V[i - 1, j] - 1
                left = self.V[i, j - 1] - 1
                maxValue = max(diag, up, left)
                self.V[i, j] = maxValue
                if diag == maxValue:
                    self.G.add_edge(self.getNodeIDfromIndex(i, j), self.getDiagNodeId(i, j))
                if up == maxValue:
                    self.G.add_edge(self.getNodeIDfromIndex(i, j), self.getUpNodeId(i, j))
                if left == maxValue:
                    self.G.add_edge(self.getNodeIDfromIndex(i, j), self.getLeftNodeId(i, j))

    def getOptScore(self):
        return self.V[-1, -1]

    def getNodeIDfromIndex(self, i, j):
        if i < 0 or j < 0 or i > self.n or j > self.m:
            raise Exception("i or j incorrect bound" + ": i : " + str(i) + " j: " + str(j))
        return (self.m + 1) * i + j

    def getLeftNodeId(self, i, j):
        return self.getNodeIDfromIndex(i, j - 1)

    def getUpNodeId(self, i, j):
        return self.getNodeIDfromIndex(i - 1, j)

    def getDiagNodeId(self, i, j):
        return self.getNodeIDfromIndex(i - 1, j - 1)



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
    print(nw.V)
    print(nw.delta(3, 6))

    nw2 = NeedlemanWunsch("ACAATCC", "AGCATGC")
    print(nw2.V)
    print(nw2.delta(1, 2))
    nw2.V[3, 2] = 8
    nw2.calc()
    print(nw2.V)

    print(list(nw2.G.nodes))
    print(list(nw2.G.edges))

    # print(nw2.getNodeIDfromIndex(7, 7))
    # print(nw2.getNodeIDfromIndex(7, 0))
    # print(nw2.getNodeIDfromIndex(0, 7))
    # print(nw2.getNodeIDfromIndex(0, 8))
    for path in nx.all_simple_paths(nw2.G, 63, 0):
        print(path)


if __name__ == '__main__':
    main()

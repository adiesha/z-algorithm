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
        self.noOfOPTAlignments = 0

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

        target = 0
        source = self.getNodeIDfromIndex(self.n, self.m)
        paths = nx.all_simple_paths(self.G, source, target)
        for path in paths:
            self.noOfOPTAlignments += 1

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

    def getAllAlginments(self):
        target = 0
        source = self.getNodeIDfromIndex(self.n, self.m)
        paths = nx.all_simple_paths(self.G, source, target)
        s = self.s
        t = self.t

        index = 1
        for path in paths:
            sStack = []
            tStack = []
            print("Optimal Alignment: ", str(index))
            for i in range(0, len(path) - 1):
                currentN = path[i]
                nextN = path[i + 1]

                ini = currentN // (self.m + 1)
                inj = currentN % (self.m + 1)

                # print(ini, inj)

                if self.isLeftNode(currentN, nextN):
                    # print(str(currentN) + " " + str(nextN) + " Left")
                    sStack.append(colors.RED + "_" + colors.ENDC)
                    tStack.append(colors.RED + self.t[inj - 1] + colors.ENDC)

                if self.isUpNode(currentN, nextN):
                    # print(str(currentN) + " " + str(nextN) + " Up")
                    sStack.append(colors.YELLOW + self.s[ini - 1] + colors.ENDC)
                    tStack.append(colors.YELLOW + "_" + colors.ENDC)

                if self.isDiagNode(currentN, nextN):
                    # print(str(currentN) + " " + str(nextN) + " Diag")
                    startColor = colors.GREEN if self.s[ini - 1] == self.t[inj - 1] else colors.BLUE
                    endColor = colors.ENDC
                    sStack.append(startColor + self.s[ini - 1] + endColor)
                    tStack.append(startColor + self.t[inj - 1] + endColor)

            # print("+++")
            while sStack:
                print(sStack.pop(), end=' ')
            print("\n")
            while tStack:
                print(tStack.pop(), end=' ')
            print("\n")
            index += 1

    def isLeftNode(self, id1, id2):
        return id1 - 1 == id2

    def isDiagNode(self, id1, id2):
        m = self.m
        return id1 - (m + 1) - 1 == id2

    def isUpNode(self, id1, id2):
        m = self.m
        return id1 - (m + 1) == id2

    def getNoOfOPTAlignments(self):
        return self.noOfOPTAlignments


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


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


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

    for path in nx.all_simple_paths(nw2.G, 63, 0):
        print(path)

    nw2.getAllAlginments()


if __name__ == '__main__':
    main()

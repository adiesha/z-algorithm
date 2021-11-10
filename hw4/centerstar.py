import sys

import numpy as np

from hw4.editdistance import EditDistance


class CenterStar():
    def __init__(self):
        self.sequences = []
        self.k = 0
        self.matrix = None
        self.rowsums = {}
        self.minrow = None

    def addsequence(self, s):
        self.sequences.append(s)
        self.k += 1

    def calculateCenterSequence(self, delta=lambda x, y: 1 if x != y else 0):
        self.matrix = np.full(shape=(self.k, self.k), fill_value=0)
        for i in range(len(self.sequences)):
            for j in range(i + 1, len(self.sequences)):
                ed = EditDistance(self.sequences[i], self.sequences[j], delta)
                ed.calc()
                self.matrix[i, j] = ed.getOptScore()
                self.matrix[j, i] = ed.getOptScore()

        min = sys.maxsize
        for i in range(len(self.sequences)):
            self.rowsums[i] = sum(self.matrix[i])
            if self.rowsums[i] < min:
                min = self.rowsums[i]
                self.minrow = i

    def getCenterSequenceIndex(self):
        return self.minrow

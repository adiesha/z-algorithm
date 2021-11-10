import sys

from hw4.centerstar import CenterStar
from utlis.readFasta import Fasta


def main():
    fileName = sys.argv[1]
    fasta = Fasta(fileName)
    cs = CenterStar()
    for v in fasta.data.values():
        cs.addsequence(v)
    print(cs.sequences)
    print(cs.k)
    cs.calculateCenterSequence(lambda x, y: 1 if x != y else 0)
    print(cs.matrix)
    print(cs.rowsums)
    print(cs.minrow)
    print(cs.getCenterSequenceIndex())


if __name__ == '__main__':
    main()

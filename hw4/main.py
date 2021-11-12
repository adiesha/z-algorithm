import sys

from hw4.centerstar import CenterStar
from utlis.readFasta import Fasta


def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    print(
        colors.YELLOW + "First two steps of center start algorithm on set of fasta files" + colors.YELLOW + colors.ENDC)

    for i in range(1, len(sys.argv)):
        fileName = sys.argv[i]
        print(colors.BLUE + "File Name: " + colors.ENDC + colors.YELLOW + fileName + colors.ENDC)
        fasta = Fasta(fileName)
        cs = CenterStar()
        for v in fasta.data.values():
            cs.addsequence(v)
        print(colors.GREEN + "Set of sequences in the file" + colors.ENDC)
        print(colors.BLUE + str(cs.sequences) + colors.ENDC)
        print(colors.BLUE + "Number of sequences: " + str(cs.k) + colors.ENDC)
        cs.calculateCenterSequence(lambda x, y: 1 if x != y else 0)
        print(
            colors.RED + "Edit Distance matrix for all the sequences that defines the distance between each other" + colors.ENDC)
        print(cs.matrix)
        print(colors.BLUE + "Row Sums in the matrix" + colors.ENDC)
        print(cs.rowsums)
        print(colors.BLUE + "Minimum Row index: " + colors.RED + str(cs.minrow) + colors.ENDC)
        print(colors.BLUE + "Center Sequence: " + colors.GREEN + str(
            cs.sequences[cs.getCenterSequenceIndex()]) + colors.ENDC)

class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


if __name__ == '__main__':
    main()

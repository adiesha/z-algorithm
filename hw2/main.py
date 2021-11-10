import sys

from needlemanwunsch import NeedlemanWunsch
from utlis.readFasta import Fasta


def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    print(colors.BLUE + "Testing for Q3 with Bonus point modification" + colors.ENDC)
    print(colors.GREEN + "Reading fasta files" + colors.ENDC)

    for i in range(1, len(sys.argv)):
        fastaName = sys.argv[i]
        print(fastaName)
        fasta = Fasta(fastaName)
        data = fasta.getData()
        print("Data in the file: ", fastaName)
        print(data)
        nw = NeedlemanWunsch(data.get(1), data.get(2))
        nw.calc()
        print(colors.BLUE + "Printing Dynamic Programming Table" + colors.ENDC)
        print(colors.GREEN + str(nw.V) + colors.ENDC)
        print(colors.BLUE + "Optimal Alignment score: " + colors.ENDC, str(nw.getOptScore()))
        print("Number of Optimal Alignments: ", nw.getNoOfOPTAlignments())
        print("Optimal Alignments ->")
        nw.getAllAlginments()


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


if __name__ == '__main__':
    main()

from needlemanwunsch import NeedlemanWunsch
from readFasta import Fasta


def main():
    fasta1 = Fasta("global1.fasta")
    data = fasta1.getData()
    print(data)
    nw = NeedlemanWunsch(data.get(1), data.get(2))
    nw.calc()
    print(nw.getOptScore())

    fasta2 = Fasta("global2.fasta")
    data = fasta2.getData()
    print(data)
    nw = NeedlemanWunsch(data.get(1), data.get(2))
    nw.calc()
    print(nw.V)
    print(nw.getOptScore())


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


if __name__ == '__main__':
    main()

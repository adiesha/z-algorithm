import sys

from main import colors
from match import ExactMatch
from readFasta import Fasta


def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    print(colors.BLUE + "Testing for bonus problem" + colors.ENDC)
    print(colors.GREEN + "Reading test.fasta file" + colors.ENDC)
    fasta = Fasta(sys.argv[2])
    data = fasta.getData()
    pattern = sys.argv[1]
    print(
        colors.YELLOW + "Iterate all the sequences in the file and run the exact pattern matching on the pattern: " + colors.ENDC + colors.RED +
        pattern + colors.ENDC)
    print(colors.YELLOW + "Number of sequences in the file: " + colors.ENDC + colors.RED + str(
        len(data.keys())) + colors.ENDC)
    for id, seq in data.items():
        print("Sequence: " + str(id))
        z = ExactMatch(seq, pattern, "$")
        print("input: " + seq + " pattern: " + pattern)
        print("Number of matches: " + str(len(z.getMatches())))
        print("matching indices in the input string: " + str(z.getMatches()))


if __name__ == '__main__':
    main()

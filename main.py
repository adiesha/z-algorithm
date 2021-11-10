from match import ExactMatch
from utlis.readFasta import Fasta


def main():
    prob2()
    probBonus()


def prob2():
    # test Exact pattern matching algorithm
    print(colors.GREEN + "Testing for problem 1 exact pattern matching algorithm" + colors.ENDC)
    z = ExactMatch("aabbabaaa", "baba", "$")
    print("input: " + "aabbabaaa" + " pattern: " + "baba")
    print("matching indices in the input string: " + str(z.getMatches()))

    z = ExactMatch("aabbabaaa", "aba", "$")
    print("input: " + "aabbabaaa" + " pattern: " + "aba")
    print("matching indices in the input string: " + str(z.getMatches()))

    z = ExactMatch("aabbabaaa", "aa", "$")
    print("input: " + "aabbabaaa" + " pattern: " + "aa")
    print("matching indices in the input string: " + str(z.getMatches()))

    z = ExactMatch("aaaaaaaaa", "aa", "$")
    print("input: " + "aaaaaaaaa" + " pattern: " + "aa")
    print("matching indices in the input string: " + str(z.getMatches()))

    input = "gtttacacggcagcctttctttatgaatatctggttgcctttgctcaagttaatccacatcagaccactacccctgagtctagcccggatcaaggctgcc"
    pattern = "ttgc"
    z = ExactMatch(input, pattern, "$")
    print("input: " + str(input) + " pattern: " + str(pattern))
    print("matching indices in the input string: " + str(z.getMatches()))

    input = "cgactgcctatacatgacaagtcgtcttccgtcctatcttgtatcgcagtggggcgctcagggtattacaatgccgccatctaccctctcgcccttgccgggcaacatgagaggggcaaagcaggtccccgtaaggccagcgaccctttgagttacaagctatcactgtcggatggggtcactatggtaatacaggtacttgaaactagtgacggatcccactacgccttcgcgcttcagcgcggactggtgggaggtcaggcagcgcatgtttcatgtcctcagaacagttcattcactgagaggacaatcactctaagctggatcaggaatgcgaacccaaggcctcaatgtagctcggggcgcgtcgtaagagaggaggcaaacattaatacgcgggtagatgcgggacttgtgatgcgcacatttttgtatatgtgtttaaaatagttttgtggagaagacatgacattggtgtgttccgatgaacgcgcatggcaggatcaagcatatggaacgatggggccaagtgcaatcagaaagtctacggggtgtgtccatttttatttcggtcgtgtgtcttacataccgaaaggttcccattgatattcggagcgcccaatctgtacgttcaaacggtatcggtttgaccggaccaagacaagtaaaccttttgttagagcagagaaggcttactgagtaacgacaggccggcctcttcagcacgggtagaggtggactgaagggcgcacaactggccgtaagatgattacaaattactggttttacgcgaatacgctttttacgttggcctacagtaagtaacagacttaccgcgcaggcaactttacatttaaactgcaatactccggaacgctagtaggctcgggagcccggacaattttaacgccctaactgggacttcctgtaagcgggatctgtgttcacatggggcctgtgcacctgtttcgcccaagaatacgcatggcgtgttttacct"
    pattern = "gcctc"
    z = ExactMatch(input, pattern, "$")
    print("input: " + input)
    print("pattern: " + pattern)
    print("matching indices in the input string: " + str(z.getMatches()))


def probBonus():
    print(colors.BLUE + "Testing for bonus problem" + colors.ENDC)
    print(colors.GREEN + "Reading test.fasta file" + colors.ENDC)
    fasta = Fasta("test.fasta")
    data = fasta.getData()
    pattern = "gagt"
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


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


if __name__ == '__main__':
    main()

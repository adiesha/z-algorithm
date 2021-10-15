import sys

from hw3.SA import SA


def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    # print(colors.BLUE + "Testing for Q3 with Bonus point modification" + colors.ENDC)
    # print(colors.GREEN + "Reading fasta files" + colors.ENDC)
    print(colors.BLUE + "Note that arrays starts from 0" + colors.ENDC)
    for i in range(1, len(sys.argv)):
        s = sys.argv[i]
        sa = SA(s)
        print(colors.BLUE + "String:-> " + colors.ENDC + colors.GREEN + s + colors.ENDC)
        print(colors.RED + str(sa.sa) + colors.ENDC)

    # s1 = "banana$"
    # s2 = "missisipi$"
    # s3 = "abracadabra$"
    # s4 = "gacgaacgac$"
    #
    # print("Note that arrays starts from 0")
    # sa1 = SA(s1)
    # print("String:-> " + s1)
    # print(sa1.sa)
    #
    # sa2 = SA(s2)
    # print("String:-> " + s2)
    # print(sa2.sa)
    #
    # sa3 = SA(s3)
    # print("String:-> " + s3)
    # print(sa3.sa)
    #
    # sa4 = SA(s4)
    # print("String:-> " + s4)
    # print(sa4.sa)

    sg = "gacgaacgac$"
    sgsa = SA(sg)
    print(colors.BLUE + "FM-index for string:-> " + colors.ENDC + colors.GREEN + sg + colors.ENDC)
    print(colors.BLUE + "Burrows Wheeler array: " + colors.ENDC)
    print(colors.RED + str(sgsa.bw) + colors.ENDC)
    print(colors.BLUE + "Count array: " + colors.ENDC)
    print(colors.RED + str(sgsa.C) + colors.ENDC)
    print(colors.BLUE + "Occ data structure: " + colors.ENDC)
    print(colors.RED)
    sgsa.printoccds()
    print(colors.ENDC)

    print(colors.YELLOW + "Bonus Question" + colors.ENDC)
    print(colors.BLUE + "Testing the binary search algo on suffix array for pattern matching" + colors.ENDC)
    pattern = "gaa"
    print(
        colors.BLUE + "String-> " + colors.ENDC + colors.GREEN + sg + colors.ENDC + colors.BLUE + " pattern-> " +
        colors.ENDC + colors.GREEN + pattern + colors.ENDC)
    (q, suffix) = sgsa.binarysearchsa(pattern)
    if q:
        print(colors.BLUE + "Pattern found in suffix: " + colors.ENDC + colors.RED + suffix + colors.ENDC)
    else:
        print(colors.RED + "Pattern not found" + colors.ENDC)

    pattern = "gcc"
    print(
        colors.BLUE + "String-> " + colors.ENDC + colors.GREEN + sg + colors.ENDC + colors.BLUE + " pattern-> " +
        colors.ENDC + colors.GREEN + pattern + colors.ENDC)
    (q, suffix) = sgsa.binarysearchsa(pattern)
    if q:
        print(colors.BLUE + "Pattern found in suffix: " + colors.ENDC + colors.RED + suffix + colors.ENDC)
    else:
        print(colors.RED + "Pattern not found" + colors.ENDC)


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


if __name__ == '__main__':
    main()

import sys

from hw3.SA import SA


def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    print(colors.YELLOW + "Demonstrating suffix array on some strings" + colors.YELLOW)
    print(colors.BLUE + "Note that arrays starts from 0" + colors.ENDC)
    for i in range(1, len(sys.argv)):
        s = sys.argv[i]
        sa = SA(s)
        print(colors.BLUE + "String:-> " + colors.ENDC + colors.GREEN + s + colors.ENDC)
        print(colors.RED + str(sa.sa) + colors.ENDC)

    print("----------------------------------------------------------")
    print(colors.YELLOW + "Demonstrating problem 2. Building FM-Index" + colors.ENDC)
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

    print("----------------------------------------------------------")

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

    print("----------------------------------------------------------")
    print(
        colors.BLUE + "Testing for problem 3, running pattern matching on string gacgaacgac with pattern gac" + colors.ENDC)
    pattern = "gac"
    s = "gacgaacgac$"
    print(colors.BLUE + "Creating FM-index for the string" + colors.ENDC)
    sa = SA(s)
    print(colors.BLUE + "Running backward search algorithm" + colors.ENDC)
    result, (start, end) = sa.backwardsearch(pattern)
    print(
        colors.RED + "Pattern: " + pattern + " found" + colors.ENDC if result else colors.RED + "pattern: " + pattern + " not found" + colors.ENDC)
    print(colors.YELLOW + "Suffix array range that contains the pattern: " + str((start, end)) + colors.ENDC)
    print(colors.BLUE + "Suffixes" + colors.ENDC)
    print(colors.GREEN)
    for i in range(start, end + 1):
        print("index " + str(sa.sa[i]) + " - " + sa.s[sa.sa[i]:])
    print(colors.ENDC)


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


if __name__ == '__main__':
    main()

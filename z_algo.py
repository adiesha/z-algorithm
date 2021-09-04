import numpy as np


def main():
    print("Hello World!")
    z = generateZi(
        "gtcaagaacgaatcacccgtcaggtactcgcccacagctgagttaatatgatactgtagagtgattttctggttctatgctgcgtcacgtagtccatatataaagattaattcacgcgccggaaagataagcattttaatgcgtcatgctatacgctgatatcgtggtctgcggtacacaagccgtcgtaataggcggcaaagcgtagagagtatgagtattctataccacggcccactctggccacgactcgactcaggcctgggaacagttacgtaaccattataacattcttagagcgacacctgcctgcacgtcaccttataacccagtagtatcttataaagtcgaaccgatacctcgtactaagccgtcacgcgtgatatctcttacggggacctaatcaacgtttgaagcaaattagcattccggaataggaattgtacgagccaaacgaataggttcggcgccgaaatccttgaaggccttacaaagcgccgctaatggtagtgacgcgtctgtgatgatgcttagcggcattggaatcggtaaaccggacgctaagttaccgttaaggccagtcgataatcttgacggttctaaatggtgccccttcctagtaaagcctagggctttcgagttcacgtccccacttaggtatccactgcaaggcttcgccaaagcgggcttgtgtacaatggaaggcaacatcgaaggtacagctcgcacgtagggtgcactcgtaggcgctaacgcgtccacttatcggttctggtcaagtttttaacgtgtgctgagtcacagctgtatttggccgaatgaaaagccgagtcccaagagacttctgcaacgaagtccctgccgtgttgagatcaacgggtgtctggaggcggcgcatctccatatagatgttaccacagaactcctgagacaggctcgcaccaccctcagcgagagtatagtacatacggacaatgtacaccctagcttcgtgggcagg")
    print(z)
    c = compare("ababb", 0, 3)
    print(c)


def generateZi(data):
    print("started")
    l = 0
    r = 0
    z_i = np.zeros((len(data),), dtype=np.int)
    z_i[0] = len(data)
    for k in range(1, len(data)):
        if k > r:
            z_k = compare(data, 0, k)
            if z_k > 0:
                r = k + z_k - 1
                l = k
                z_i[k] = z_k
            else:
                z_i[k] = 0

        else:
            kprime = k - l + 0
            beta = r - k + 1
            z_kprime = z_i[kprime]
            if z_kprime < beta:
                z_k = z_kprime
                z_i[k] = z_k
            else:
                c = compare(data, beta + 0, r + 1)
                q = r + c + 1
                z_i[k] = q - k
                l = k
                r = q - 1
    return z_i


def compare(data, i, j):
    """
    This method will take input string two indices and read compare characters from index i and j until it finds a mismatch
    Then it will return the number of successful consecutive matches as the output
    :param data: the string input
    :param i: i < j starting index 1
    :param j: i < j starting index 2
    :return: number of consecutive matches
    """

    l = len(data)
    count = 0

    while j < l:  # until we reach the end of the string
        if data[i] == data[j]:
            count = count + 1
            i = i + 1
            j = j + 1
        else:
            break
    return count


if __name__ == "__main__":
    main()

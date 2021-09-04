from z_algo import generateZi


def main():
    print("Hello")
    z = ExactMatch("aabbabaaa", "baba", "$")
    print(z.getMatches())


class ExactMatch():

    def __init__(self, data, pattern, sepChar):
        self.pattern = pattern
        self.sepChar = sepChar
        self.zlist = self.createZiList(data, pattern, sepChar)

    def createZiList(self, data, pattern, sepChar):
        input = pattern + sepChar + data
        zlist = generateZi(input)
        return zlist

    def getMatches(self):
        patternSize = len(self.pattern)
        matches = []
        count = 0
        for i in self.zlist:
            if i == patternSize:
                matches.append(count - patternSize - len(self.sepChar))
            count = count + 1
        return matches


if __name__ == '__main__':
    main()

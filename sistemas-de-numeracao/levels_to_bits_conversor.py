from math import log


def convertDecimalToBinary(value: str or int):
    number = int(value)
    string = ''

    while number > 0:
        rest = int(number % 2)
        string += str(rest)
        number = (number - rest) / 2

    return string[::-1]


def convertLevelsToBit(levels: int):
    bitCombinations = []
    #totalBits = int(levels / log(2))

    for i in range(0, levels):
        bitCombinations.append(convertDecimalToBinary(i))

    print(bitCombinations)
    # print(totalBits)


convertLevelsToBit(int(input("Entre com o número de níveis: ")))

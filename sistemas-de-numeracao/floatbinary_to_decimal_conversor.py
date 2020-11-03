def revertBinary(binaryString: str):
    result = 0
    stringToList = list(binaryString)

    for i in range(len(stringToList)):
        currentValue = int(stringToList[i])
        if(currentValue != 1 and currentValue != 0):
            return "Por favor, o valor deve estar em binário! Tente novamente."
        else:
            result += currentValue * \
                2 ** (len(stringToList) - i - 1)

    return result


def convertFloatBinary(value: str):
    stripInPoint = str(value).split(',')
    positiveExpos = revertBinary(stripInPoint[0])
    negativeExpos = list(stripInPoint[1])
    floatNumber = 0

    for i in range(0, len(negativeExpos)):
        currentNumber = int(negativeExpos[i])
        floatNumber += currentNumber * 2 ** - (i + 1)

    return positiveExpos + floatNumber


print(convertFloatBinary(input("Digite o valor fracionário em binário: ")))

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


print(revertBinary(input("Define um valor em binário: ")))

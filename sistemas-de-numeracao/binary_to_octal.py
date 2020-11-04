# ajusta os valores para grupos de 3 bits
def adjustBinaryValue(value):
    stringToList = list(value)
    invertList = stringToList[::-1]

    while len(stringToList) % 3 != 0:
        invertList.append('0')
        stringToList = invertList[::-1]

        if(len(stringToList) % 3 == 0):
            break

    return stringToList


# cria os grupos de 3 bits cada
def createBitsGroups(value):
    adjustValue = adjustBinaryValue(value)
    groups = []
    lastGroupNumber = 0

    for i in range(0, len(adjustValue)):
        if((i + 1) % 3 == 0):
            groups.append(adjustValue[lastGroupNumber:i+1])
            lastGroupNumber = i + 1

    return groups


# multiplica os valores dos grupos
def multiplyGroupsValue(number):
    createGroups = createBitsGroups(number)

    for i in range(len(createGroups)):
        for j in range(len(createGroups[i])):
            createGroups[i][j] = str(
                int(createGroups[i][j]) * 2 ** (len(createGroups[i]) - j - 1))

    return createGroups


# gerencia a entrada e soma os resultados finais dos grupos
def convertBinaryToOctal(number):
    createGroupsAndMultiply = multiplyGroupsValue(number)
    response = ''

    for i in range(len(createGroupsAndMultiply)):
        finalGroupValue = 0

        for j in range(len(createGroupsAndMultiply[i])):
            finalGroupValue += int(createGroupsAndMultiply[i][j])

        response += str(finalGroupValue)

    return response


print(convertBinaryToOctal(input("Informe o valor em binário: ")))

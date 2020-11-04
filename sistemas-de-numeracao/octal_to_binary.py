def convertDecimalToBinary(value: str or int):
    number = int(value)
    string = ''

    while number > 0:
        rest = int(number % 2)
        string += str(rest)
        number = (number - rest) / 2

    return string[::-1]


def octalToDecimal(value: str):
    reverseValue = value[::-1]
    response = 0

    for i in range(0, len(value)):
        response += int(reverseValue[i]) * 8 ** i

    return convertDecimalToBinary(response)


print(octalToDecimal(input("Informe o valor em octal: ")))

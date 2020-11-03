def convertDecimalToBinary(value: str or int):
    number = int(value)
    string = ''

    while number > 0:
        rest = int(number % 2)
        string += str(rest)
        number = (number - rest) / 2

    return string[::-1]


while True:
    print(convertDecimalToBinary(input("Informe o valor em decimal: ")))

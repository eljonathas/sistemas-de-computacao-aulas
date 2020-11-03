def convertDecimalToBinary(value: str or int):
    number = int(value)
    string = ''

    while number > 0:
        rest = int(number % 2)
        string += str(rest)
        number = (number - rest) / 2

    return string[::-1]


def convertFloatDecimal(number):
    decimal, floatpoint = str(number).split(".")
    decimal = int(decimal)
    floatpoint = int(floatpoint)
    res = convertDecimalToBinary(decimal) + "."

    for i in range(3):
        decimal, floatpoint = str(
            (decimalConverter(floatpoint)) * 2).split(".")
        floatpoint = int(floatpoint)
        res += decimal

    return res


def decimalConverter(num):
    while num > 1:
        num /= 10
    return num


while True:
    print(convertFloatDecimal(input("Informe o valor fracionário em decimal: ")))

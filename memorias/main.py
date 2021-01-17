memo = []


def setInitialCellState(q):
    # q quantidade de bits
    cell = []
    for i in range(0, q):
        cell.append(0)
    return cell


def setInitialMemoState(b, c):
    # b = bits da palavra, c = quantidade de células
    for i in range(0, c):
        memo.append(setInitialCellState(b))


def showCellData(e):
    if memo[e]:
        return ''.join(str(i) for i in memo[e])
    return False


def addresSize():
    for i in range(0, len(memo)):
        if 2 ** i >= len(memo):
            return i


def setCellData(d, e):
    if memo[e]:
        if len(d) == len(memo[e]):
            memo[e] = d
            return True
    return False


def showMemo():
    # retorna o estado total da memória
    for i in range(0, len(memo)):
        print(''.join(str(e) for e in memo[i]))
    print()


def binToDec(b):
    # faz a conversão do endereço binário para decimal
    result = 0
    stringToList = list(b)

    for i in range(len(stringToList)):
        currentValue = int(stringToList[i])
        if(currentValue != 1 and currentValue != 0):
            return "Por favor, o valor deve estar em binário! Tente novamente."
        else:
            result += currentValue * \
                2 ** (len(stringToList) - i - 1)

    return result


def initMemo():
    setInitialMemoState(8, 16)
    showMemo()


initMemo()

while True:
    print("Digite W para escrever, R para ler, L para listar e qualquer outra teclar para sair.")
    option = input("").lower()

    if option == 'w':
        address = binToDec(
            input(f'Informe o endereço de {addresSize()} bits: '))
        value = list(
            input(f'Informe o dado de {len(memo[0])} bits: '))
        if setCellData(value, address):
            showMemo()
        else:
            print("Um erro ocorreu na gravação dos dados")
    elif option == 'r':
        address = binToDec(
            (input(f'Informe o endereço de {addresSize()} bits: ')))
        print(showCellData(address))
    elif option == 'l':
        showMemo()
    else:
        exit()
    print()

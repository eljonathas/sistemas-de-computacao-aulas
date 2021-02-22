from random import randint

MP = []
CACHE = []
REG = ""
CI = 0


def mpInitiator(cells: int, size: int):
    # Inicializa a memória principal com a quantidade de células definida como parâmetro
    for x in range(cells):
        cell = []
        for y in range(size):
            cell.append(0)
        MP.append(cell)


def cacheInitiator(cells: int, size: int):
    # Inicializa a memória cache com a quantidade de células definida como parâmetro
    for l in range(cells):
        cell = []
        for y in range(size):
            cell.append(0)
        CACHE.append(cell)


def mpController(action: bool, addres: str, data: str):
    decimalAddress = numberConversor(addres, 'bin->dec', 8)

    # true = Gravação / false = Leitura
    if(action):
        if len(data) < len(MP[0]):
            tmpData = list(data)
            tmpData.reverse()
            while len(tmpData) < len(MP[0]):
                tmpData.append(0)
            MP[decimalAddress] = tmpData[::-1]
        elif len(data) > len(MP[0]):
            return print(f"Error: o tamanho da palavra não pode exceder o tamanho de {len(MP[0])} bits.")
        else:
            MP[decimalAddress] = list(data)
            return print(f"Success: o dado foi armazenado no index {decimalAddress} da memória.")
    else:
        return ''.join(str(i) for i in MP[decimalAddress])


def cacheController(address: str):
    byteField = numberConversor(address[6::], 'bin->dec', 8)
    groupField = numberConversor(address[4:6], 'bin->dec', 8)
    tagField = numberConversor(address[0:4], 'bin->dec', 8)

    groups = [CACHE[0:4], CACHE[4:8], CACHE[8:12], CACHE[12:16]]
    currentGroup = groups[groupField]

    for x in range(len(currentGroup)):
        dataToString = ''.join(str(i) for i in currentGroup[x])
        currentTagField = numberConversor(dataToString[0:4], 'bin->dec', 8)
        bytesInLine = [dataToString[40::], dataToString[28:40],
                       dataToString[16:28], dataToString[4:16]]

        if int(tagField) == int(currentTagField):
            # verifica se o dado é realmente o que o usuário quer fazendo um pulso a mp
            dataInMp = ''.join(str(i)
                               for i in MP[numberConversor(address, 'bin->dec', 8)])

            if bytesInLine[byteField] == dataInMp:
                return bytesInLine[byteField]

    # se chegar nesse ponto, significa que não achou (miss)
    newCell = []
    tmpCell = []
    conjAddress = 0

    for l in range(len(MP)):
        currentAddress = str(numberConversor(l, 'dec->bin', 9))
        currentAddress = currentAddress[1::]
        blockAddress = currentAddress[0:6]

        if address[0:6] == blockAddress:
            conjAddress = int(numberConversor(
                "".join(str(e) for e in blockAddress[4:6]), "bin->dec", 8))

            for x in MP[l]:
                newCell.append(x)

    newCell = [list(address[0:4]), newCell[36:48], newCell[24:36],
               newCell[12:24], newCell[0:12]]

    for l in range(len(newCell)):
        for x in newCell[l]:
            tmpCell.append(x)

    newCell = tmpCell

    if len(newCell) == 52:
        randomValue = randint(conjAddress-1, conjAddress+1)
        CACHE[randomValue] = newCell

        bytesInLine = [newCell[40::], newCell[28:40],
                       newCell[16:28], newCell[4:16]]

        return ''.join(str(x) for x in bytesInLine[byteField])

    else:
        return print("Error")


def numberConversor(value, type, size):
    convertedValue = 0

    if type == "dec->bin":
        # efetua a conversão do valor em decimal para binário
        number = int(value)
        string = ''

        while number > 0:
            rest = int(number % 2)
            string += str(rest)
            number = (number - rest) / 2

        if(len(string) < size):
            tmpList = list(string)

            while len(tmpList) < size:
                tmpList.append('0')

            convertedValue = ''.join(tmpList[::-1])

    if type == "bin->dec":
        # faz a conversão do valor em binário para decimal
        result = 0
        stringToList = list(value)

        for i in range(len(stringToList)):
            currentValue = int(stringToList[i])
            if(currentValue != 1 and currentValue != 0):
                return print("Por favor, o valor deve estar em binário! Tente novamente.")
            else:
                result += currentValue * \
                    2 ** (len(stringToList) - i - 1)

        convertedValue = int(result)

    return convertedValue


# inicializa a memória principal definindo o tamanho de cada célula e a quantidade de células
mpInitiator(256, 12)
# inicializa a memória cache definindo o tamanho de cada célula e a quantidade de células
# nesse caso, como a mp será composta por blocos de 4 bytes, cada linha terá 4 bytes de tamanho + 4 bits pro tag
# e um total de 16 linhas / 4 linhas = 4 conjuntos -> - 4 bit pro tag - 2 bits pro conjunto - 2 bits pro campo byte
cacheInitiator(16, 52)

while True:
    print("""
    Selecione uma opção:
    1 - Carregar programa
    2 - Visualizar MP
    3 - Visualizar cache
    """)
    cmd = int(input(""))

    # o comando 1 inicializa o programa proposto na atividade
    if cmd == 1:
        # mantém a execução do programa enquanto o runner estiver em nível alto
        runner = True

        # grava a instrução 1b4 no endereço 00
        mpController(True, '00000000', '000110110100')
        # grava a instrução 4b5 no endereço 01
        mpController(True, '00000001', '010010110101')
        # grava a instrução 705 no endereço 02
        mpController(True, '00000010', '011100000101')
        # grava a instrução ab4 no endereço 03
        mpController(True, '00000011', '101010110100')
        # grava a instrução 806 no endereço 04
        mpController(True, '00000100', '100000000110')
        # grava a instrução ab5 no endereço 05
        mpController(True, '00000101', '101010110101')
        # grava a instrução 000 (end) no endereço 06
        mpController(True, '00000110', '000000000000')
        # grava o valor 2b3 na posíção b4
        mpController(True, '10110100', '001010110011')
        # grava o valor 1a3 na posíção b5
        mpController(True, '10110101', '000110100011')

        while CI < 7:
            binCI = numberConversor(CI, "dec->bin", 9)
            parseBin = str(cacheController(binCI[1::]))

            CI += 1

            # FUNÇÃO DE LOAD
            if parseBin[0:4] == "0001":
                print("Instrução 0001 - LDA:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {cacheController(parseBin[4::])}")
                print(f"RI: {parseBin}")
                print(f"Reg: {REG}")

            # FUNÇÃO DE STORE
            if parseBin[0:4] == "0010":
                REG = cacheController(parseBin[4::])
                print("Instrução 0010 - STR:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {REG}")
                print(f"Reg0: {REG}")
                print(f"RI: {parseBin}")

            # FUNÇÃO DE ADIÇÃO
            if parseBin[0:4] == "0011":
                result = int(numberConversor(REG, 'bin->dec', 8)) + \
                    int(numberConversor(cacheController(
                        parseBin[4::]), 'bin->dec', 8))
                REG = numberConversor(result, 'dec->bin', 9)
                REG = REG[1::]

                print("Instrução 0011 - ADD:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {cacheController(parseBin[4::])}")
                print(f"Reg0: {REG}")
                print(f"RI: {parseBin}")

            # FUNÇÃO DE SUBTRAÇÃO
            if parseBin[0:4] == "0100":
                result = int(numberConversor(REG, 'bin->dec', 8)) - \
                    int(numberConversor(cacheController(
                        parseBin[4::]), 'bin->dec', 8))
                REG = numberConversor(result, 'dec->bin', 9)
                REG = REG[1::]

                print("Instrução 0100 - SUB:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {cacheController(parseBin[4::])}")
                print(f"Reg0: {REG}")
                print(f"RI: {parseBin}")

            # FUNÇÃO JZ
            if parseBin[0:4] == "0101":
                tmpReg = numberConversor(
                    cacheController(parseBin[4::]), 'bin->dec', 8)
                if tmpReg == 0:
                    CI = tmpReg

                print("Instrução 0101 - JZ:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {cacheController(parseBin[4::])}")
                print(f"Reg0: {REG}")
                print(f"CI: {numberConversor(CI, 'dec->bin', 9)}")

            # FUNÇÃO JP
            if parseBin[0:4] == "0110":
                tmpReg = numberConversor(
                    cacheController(parseBin[4::]), 'bin->dec', 8)
                if tmpReg > 0:
                    CI = tmpReg

                print("Instrução 0110 - JP:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {cacheController(parseBin[4::])}")
                print(f"Reg0: {REG}")
                print(f"CI: {numberConversor(CI, 'dec->bin', 9)}")

            # FUNÇÃO JM
            if parseBin[0:4] == "0111":
                tmpReg = numberConversor(
                    cacheController(parseBin[4::]), 'bin->dec', 8)
                if tmpReg < 0:
                    CI = tmpReg

                print("Instrução 0111 - JN:")
                print(f"REM: {parseBin[4::]}")
                print(f"RDM: {cacheController(parseBin[4::])}")
                print(f"Reg0: {REG}")
                print(f"CI: {numberConversor(CI, 'dec->bin', 9)}")

            # FUNÇÃO JUMP
            if parseBin[0:4] == "1000":
                tmpReg = numberConversor(
                    cacheController(parseBin[4::]), 'bin->dec', 8)

                print("Instrução 1000 - JUMP:")
                if tmpReg != 0:
                    CI = tmpReg
                    print(f"REM: {parseBin[4::]}")
                    print(f"RDM: {cacheController(parseBin[4::])}")
                    print(f"Reg0: {REG}")
                    print(f"CI: {numberConversor(CI, 'dec->bin', 9)}")
                else:
                    print(
                        "Função JUMP não executada por falta de informação no operador")

            # FIM DO PROGRAMA
            if parseBin[0:4] == "0000":
                print("Instrução 0000 - HLT:")
                print("Fim da execução")
    if cmd == 2:
        # visualiza o estado atual da MP
        for i in range(0, len(MP)):
            print(''.join(str(e) for e in MP[i]))
        print()
    if cmd == 3:
        # visualiza o estado atual do cache
        for i in range(0, len(CACHE)):
            print(''.join(str(e) for e in CACHE[i]))
        print()

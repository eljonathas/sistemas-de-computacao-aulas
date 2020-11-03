import itertools


def niveisToBits(value: str):
    niveisCounter = 0

    for bits in range(0, 255):
        if(niveisCounter != value):
            niveisCounter = 2 ** bits
            if value % niveisCounter != 0:
                exit(print("ERROR: Informe apenas potências de 2"))
        else:
            print(f"Número de bits: {bits - 1}")
            print("Estas são as combinações possíveis: ")

            for i in itertools.product([0, 1], repeat=(bits-1)):
                print(i)

            break


niveisToBits(int(input("Informe o número de níveis: ")))

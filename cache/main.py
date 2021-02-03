from random import choice, randrange as S
Z = ' Conjunto: 1'
Y = ' Conjunto: 0'
X = '0110'
W = '0010'
V = '1000'
U = '0000'
R = ' Dado 1: '
Q = ' Dado 0: '
P = '\nTAG: '
O = int
L = 'Endereço inválido. É preciso inserir um endereço de 4 bits.'
K = 'Digite um dado de 8 bits: '
H = input
F = print
E = '00000000'
D = len
G = {0: E, 1: E, 2: E, 3: E, 4: E, 5: E, 6: E, 7: E,
     8: E, 9: E, 10: E, 11: E, 12: E, 13: E, 14: E, 15: E}
B = {0: E, 1: E, 2: E, 3: E, 4: E, 5: E, 6: E, 7: E}
J = {0: U, 1: V, 2: W, 3: X}


def I(end, dado):
    F = '0'
    C = dado
    A = end
    I = O(A, 2)
    H = A
    if I % 2 != 0:
        H = O(A, 2)-1
        H = f"{H:04b}"
    if A in J.values() or H in J.values():
        if A == J[0]:
            if A[3] == F:
                B[0] = C
            else:
                B[1] = C
        if A == J[1]:
            if A[3] == F:
                B[2] = C
            else:
                B[3] = C
        if A == J[2]:
            if A[3] == F:
                B[4] = C
            else:
                B[5] = C
        if A == J[3]:
            if A[3] == F:
                B[6] = C
            else:
                B[7] = C
    else:
        if A[3] == F:
            D = C
            E = G[I+1]
        else:
            E = C
            D = G[I-1]
        if A[2] == F:
            H = S(1)
            if H == 0:
                J[0] = A
                if A[3] == F:
                    B[0] = D
                    B[1] = E
                else:
                    B[1] = E
                    B[0] = D
            else:
                J[1] = A
                if A[3] == F:
                    B[2] = D
                    B[3] = E
                else:
                    B[3] = E
                    B[2] = D
        else:
            H = S(1)
            if H == 0:
                J[2] = A
                if A[3] == F:
                    B[4] = D
                    B[5] = E
                else:
                    B[5] = E
                    B[4] = D
            else:
                J[3] = A
                if A[3] == F:
                    B[6] = D
                    B[7] = E
                else:
                    B[7] = E
                    B[8] = D


while True:
    M = H('Digite W para escrever, R para ler, L para listar e qualquer outra teclar para sair: ')
    if M == 'L':
        F('Endereços da memória cache: '+P +
          J[0][0:2]+Y+Q+B[0]+R+B[1]+P+J[1][0:2]+Y+Q+B[2]+R+B[3]+P+J[2][0:2]+Z+Q+B[4]+R+B[5]+P+J[3][0:2]+Z+Q+B[6]+R+B[7])
        F('Endereços memória principal:')
        for T in range(16):
            F(G[T])
    if M == 'W':
        C = H('Digite o endereço de 4 bits: ')
        if C == U:
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[0] = A
        if C == '0001':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[1] = A
        if C == W:
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[2] = A
        if C == '0011':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[3] = A
        if C == '0100':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[4] = A
        if C == '0101':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[5] = A
        if C == X:
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[6] = A
        if C == '0111':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[7] = A
        if C == V:
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[8] = A
        if C == '1001':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[9] = A
        if C == '1010':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[10] = A
        if C == '1011':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[11] = A
        if C == '1100':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[12] = A
        if C == '1101':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[13] = A
        if C == '1110':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[14] = A
        if C == '1111':
            A = H(K)
            if D(A) > 8 or D(A) < 8:
                F(L)
            else:
                I(C, A)
                G[15] = A
    if M == 'R':
        N = H('Digite um dos endereço de 4 bits: ')
        if N in J.values():
            F('Houve um HIIT')
            F(G[O(N, 2)])
        else:
            F('Houve um MISS')
            F(G[O(N, 2)])

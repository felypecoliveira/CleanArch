def soma_matrizes(A, B):
    # Verifica se as dimensões das matrizes são iguais
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    # Cria uma matriz vazia para armazenar a soma
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] + B[i][j])
        C.append(linha)

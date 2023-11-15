while True:
    N, M = map(int, input().split())
    if N == 0 or M == 0 or N < 0 or M < 0:
        break

    if N > 0 and N > M:
        soma = 0
        for i in range(M, N + 1):
            soma += i
            print(i, end=' ')
        print(f'Sum={soma}')

    if M > 0 and M > N:
        soma = 0
        for i in range(N, M + 1):
            soma += i
            print(i, end=' ')
        print(f'Sum={soma}')

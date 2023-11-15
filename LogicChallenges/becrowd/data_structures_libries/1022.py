"""
Sum: (N1*D2 + N2*D1) / (D1*D2)
Subtraction: (N1*D2 - N2*D1) / (D1*D2)
Multiplication: (N1*N2) / (D1*D2)
Division: (N1/D1) / (N2/D2), that means (N1*D2)/(N2*D1)
"""

op = input('Operando: ')
teste = int(input("case teste: "))

n1 = int(input("n1:"))
n2 = int(input("n2:"))
d1 = int(input("d1:"))
d2 = int(input("d2:"))

num = n1, d2, n2, d1
dem = d1, d2

if op == '+':
    num = (n1 * d2) + (n2 * d1)
    dem = (d1 * d2)

elif op == '-':
    num = (n1 * d2) - (n2 * d1)
    dem = (d1 * d2)


elif op == '*':
    num = (n1 * n2)
    dem = (d1 * d2)


elif op == '/':
    num = (n1 / d1)
    dem = (n2 / d2)


def fatora(a, b):
    abs_a, abs_b = abs(a), abs(b)
    menor = min(abs_a, abs_b)
    maior = max(abs_a, abs_b)
    divisor = menor
    while divisor > 1:
        if (menor % divisor) == 0:
            if (maior % divisor) == 0:
                return int(a / divisor), int(b / divisor)
        divisor -= 1
    return a, b


s_num, s_dem = fatora(num, dem)

for test in range(teste):
    print('{} / {} = {} / {} '.format(num, dem, s_num, s_dem))

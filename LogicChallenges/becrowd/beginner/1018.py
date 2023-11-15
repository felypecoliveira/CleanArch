n = int(input())
print(n)
qtd1 = n // 100
n = n % 100
qtd2 = n // 50
n = n % 50
qtd3 = n // 20
n = n % 20
qtd4 = n // 10
n = n % 10
qtd5 = n // 5
n = n % 5
qtd6 = n // 2
n = n % 2
qtd7 = n // 1
n = n % 1

print(f"{qtd1} nota(s) de R$ 100,00")
print(f"{qtd2} nota(s) de R$ 50,00")
print(f"{qtd3} nota(s) de R$ 20,00")
print(f"{qtd4} nota(s) de R$ 10,00")
print(f"{qtd5} nota(s) de R$ 5,00")
print(f"{qtd6} nota(s) de R$ 2,00")
print(f"{qtd7} nota(s) de R$ 1,00")

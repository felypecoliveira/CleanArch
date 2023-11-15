def is_narcissistic(i):
    i = int(i)
    x = [int(i) for i in str(i)]
    soma = 0

    for numero in x:
        soma += int(numero ** len(x))

    if soma == i:
        return True
    elif soma != i:
        return False


print(is_narcissistic(153))

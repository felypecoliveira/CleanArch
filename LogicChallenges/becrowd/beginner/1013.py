a, b, c = map(int, input().split())

maiorAB = int(a + b + abs(a - b)) / 2

if maiorAB > c:
    print("{:.0f} eh o maior".format(maiorAB))

if c > maiorAB:
    print("{:.0f} eh o maior".format(c))

# finalizado sem ajuda

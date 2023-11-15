N, M = map(int, input().split())

print(N, M)

a = ".|."
b = "WELCOME"
for i in range(N // 2):
    print(((2 * i + 1) * a).center(M, "-"))

print(b.center(M, "-"))

for i in reversed(range(N // 2)):
    print(((2 * i + 1) * a).center(M, "-"))

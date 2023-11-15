string = input()
k = int(input(""))

for i in range(0, len(string), k):
    substring = ''
    for j in range(k):
        if string[i + j] not in substring:
            substring = substring + string[i + j]

        else:
            continue

    print(substring)

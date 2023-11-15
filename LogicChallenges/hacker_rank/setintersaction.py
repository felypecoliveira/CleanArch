number = int(input())
n = map(int, input().split())
set1 = set(n)
number_ = int(input())
n2 = map(int, input().split())
set2 = set(n2)
intersection = set1.intersection(set2)

count = 0
for i in intersection:
    count += 1

print(count)

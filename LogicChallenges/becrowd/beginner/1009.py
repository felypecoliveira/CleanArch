nome = input()
money_saller = float(input())
total_sold = float(input())

result = (total_sold * 0.15) + money_saller

print("TOTAL = R$ {:.2f}".format(result))

age_days = int(input())
anos = age_days // 365
dias_restantes = age_days - (anos * 365)
meses = dias_restantes // 30
dias = dias_restantes - (meses * 30)

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")

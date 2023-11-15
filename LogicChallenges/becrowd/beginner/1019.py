segundos = int(input())
horas = segundos // 3600
resto_horas = segundos % 3600
minutos = resto_horas // 60
resto_minutos = segundos % 60

print(f'{horas}:{minutos}:{resto_minutos}')

km_litro = 12
trip_hours = int(input())
average_speed = int(input())
distance = trip_hours * average_speed
answer = distance / km_litro

print(f'{answer:.3f}')

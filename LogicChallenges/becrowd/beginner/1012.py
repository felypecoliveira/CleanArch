"""
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of the square that has side B.
e) the area of the rectangle that has sides A and B.
"""

point_values = input()

value1, value2, value3 = point_values.split()

value1 = float(value1)
value2 = float(value2)
value3 = float(value3)

pi = 3.14159
raio = value3 * value3

triangulo_retangulo = value1 * value3 / 2
circulo = pi * raio
trapezio = (value1 + value2) * value3 / 2
quadrado = value2 * value2
retangulo = value1 * value2

print('TRIANGULO: {:.3f}'.format(triangulo_retangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))

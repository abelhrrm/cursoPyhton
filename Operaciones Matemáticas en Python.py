#operadores numéricos 
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print("Parte entera de la división:", a // b)
print("Módulo:", a % b)

#Atajos o shortcuts agregamos al mismo valor de la variable la suma o cualquier otro operación matemática.
a = a + 2
print(a)
a += 2
print(a)
#resta
a -= 3
print(a)
#multiplicación
a *= 4
print(a)
#División
a /= 10
print(a)

#Operaciones matemáticas usando PENDAS:
#P -> Paréntesis
#E -> Exponenciación
#M -> Multiplicación
#D -> División
#A -> Adición
#S -> Sustracción

operation_1 = 2 + 3 * 4
print("operation_1:", operation_1)
operation_2 = (2+3)*4
print("operation_2:", operation_2)
operation_3 = (2+3)*(4**2)/8-1
print("operation_3:", operation_3)

#operadores booleanos
print (a > b)
print (a < b)
print (a >= b)
print (a <= b)
print (a == b)
print (a != b)
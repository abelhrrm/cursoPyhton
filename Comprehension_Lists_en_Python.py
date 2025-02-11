#Hallar los números cuadrados de los números del 1 al 10 o al 100.
#List Comprehension = [Expresion for var in iterable if condition]
squares = [x**2 for x in range(1,101)]
#print(squares)

#usar Comprehension list para allar la temperatura en Fahrenheit de una lista en grados Celcius

Celcius = [0, 10, 20, 30, 40]
Fahrenheit = [(temp* 9/5) +32 for temp in Celcius]
#print (Fahrenheit)

#Numeros pares
npares = [x for x in range (1,21) if x%2==0]
#print (npares)

#Matrix transpuesta

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print (matrix)
print (transposed)

#Código que muestra la matrix transpuesta pero que no usa Comprehension list 
transposed = []
for i in range(len(matrix[0])):
    print(i)
    transposed_row = []
    for row in matrix:
        print(transposed_row)
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    print(transposed_row)

print(transposed)
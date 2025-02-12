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

#print (matrix)
#print (transposed)

#Código que muestra la matrix transpuesta pero que no usa Comprehension list 
transposed = []
for i in range(len(matrix[0])):
   # print(i)
    transposed_row = []
    for row in matrix:
       #print(transposed_row)
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    #print(transposed_row)

#print(transposed)

"""
Doble de los Números
Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
"""

x = list((1,2,3,4,5))
y = [double*2 for double in x]
#print (y)

"""
Filtrar y Transformar en un Solo Paso
Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
"""
x_lista = ["sol", "mar", "montaña", "rio", "estrella"]
y = [filtrada.upper() for filtrada in x_lista if len(filtrada) > 3]

#print (y)

"""
Crear un Diccionario con List Comprehension
Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
"""
claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {clave:valor for clave, valor in zip (claves, valores)}
#diccionario = {claves[i]: valores[i] for i in range(len(claves))}
#print (diccionario)

"""
Extraer Información de una Lista de Diccionarios
Dada una lista de diccionarios que representan personas:

pythonCopiar código
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
"""
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}]

extraer = [validar["nombre"] for validar in personas if validar["ciudad"] == "Madrid" and validar["edad"] > 30]

#print (extraer)

"""
List Comprehension con un else
Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares_doble = [x*2 if x%2==0 else x for x in numeros]

#print #(pares_doble)
#Hallar los números cuadrados de los números del 1 al 10 o al 100.
#List Comprehension = [Expresion for var in iterable if condition]
squares = [x**2 for x in range(1,101)]
print(squares)
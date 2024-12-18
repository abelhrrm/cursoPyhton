#Las matrices en python son listas de listas
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matrix)
#Para acceder a un elemento dentro de esta matrix usamos la sintaxis matrix[1][2]
print(matrix[1][2])
#Estas son conocidas como listas mutables, quiere decier que podemos modificar un elemento de la matrix o lista de listas.
matrix[2][1]="ocho"
print(matrix[2])

#En python también existen listas inmutables, estas listas son conocidas como tuplas. Para construirlas ()
numbers = (1,2,3,4,5,6)
print(numbers)
print(type(numbers))#resultado del print <class 'tuple'>
#modificar la tupla la cual no se puede porque es una lista inmutable.

#numbers[0]="1" #Salida TypeError: 'tuple' object does not support item assignment

#Sin embargo dentro de la lista inmutable tenemos una lista mutable esta si la podemos modificar sin problemas.

numbers = (1,2,3,4,5,6,[7,8,9])
print(numbers)

#Modificar la lista mutable dentro de la tupla
numbers[6][0]="siete"
print(numbers)
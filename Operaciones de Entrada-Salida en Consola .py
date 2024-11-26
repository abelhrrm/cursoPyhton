#Usamos la función input para interactuar con el usuario por medio de la consola.
name= input("Ingrese su nombre: ")
print(f"Hola {name}")
print("Variable name", type(name))
age= input("Ingrese su edad: ")
print(int(age))

#La función input siempre entrega un string a las entradas dadas por el usuario.
#Esto es casting implícito, convierte un tipo de valor a otro en este caso a string.
#En el caso de age haremos un casting explicito convirtiendo a int.
print(type(int(age)))
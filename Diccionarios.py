#Los diccionarios en python almacenan dos datos la llave y el valor
#Tal como lo hacer los diccionarios cuya palabra es la clave y el significado es el valor.
#Estos se crear con los {}
numbers={1:"uno",2:"dos",3:"tres"}
print(numbers)

#Para acceder a una posición en el diccionario debemos dar la clave o llave completa y este retornará el valor.
print(numbers[3])

#Mas ejemplos
information = {"Nombre": "Abel",
               "Apellido": "Herrera",
               "Altura": 1.63,
               "Edad": 38}
print(information)
#Eliminar la última clave del diccionario.
del information["Edad"]
print(information)

#Metodos en los diccionarios
claves = information.keys()
valor = information.values()
pairs = information.items()
print(claves)
print(valor)
print (pairs)
print(type(information))
print(type(claves))
print(type(valor))
print(type(pairs))
#Retorno respectivo:
#<class 'dict'>
#<class 'dict_keys'>
#<class 'dict_values'>
#<class 'dict_items'>

#También podemos crear un diccionario de diccionario
contacts = {"Abel":{"Apellido": "Herrera",
               "Altura": 1.63,
               "Edad": 38},
            "Julieth":{"Apellido": "Rios",
               "Altura": 1.62,
               "Edad": 32}}
print(contacts)
print(contacts["Abel"]) #Imprime el valor de la clave "Abel"
print(contacts["Abel"]["Edad"]) #Imprime el valor de la clave "Abel" y de la clave "Edad" dentro de "Abel"
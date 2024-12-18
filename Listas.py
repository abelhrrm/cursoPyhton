# Las listas se crean  con los []
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Ir a un museo",
         "Volver al hotel"]
print(to_do)
#las listas son mutables y se pueden crear con diferentes tipos de datos
numbers=[1,2,3,4,"cinco"]
print(numbers)
print(type(numbers))

mix=["uno", 2, 3.14, True, [1,2,3]]
print(mix)
#Determinar el tamaño de la lista con la función len
print("la longitud de la lista es:", len(mix))

#Indexación en las listas nombre de variable segudio con el número de la posición [0]
print("Primer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Último elemento:", mix[-1])

#Slice en indexación se utiliza usando los dos puntos dentro de los corchetes [inicio:fin]
print(mix[1:4])
#Si dejas vacio la posición este lo tomara desde el inicio o el fin.
print(mix[2:])

#Métodos: las listas tienen su propias funciones que son conocidos como métodos.
#Para invocar el método se debe escribir el nombre de la lista seguido de un punto y el nombre del método.
print(mix)
mix.append(False)#con .append agrega un nuevo elemento a la lista al final.
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])#con .insert podemos agregar un elemento en la lista indicando la posición que queremos añadir.
print(mix)
print(mix.index(["a","b"]))#con .index podemos consultar la posición de un elemento en lista y este devolverá la primera coincidencia.

#Cuando trabajamos con lista de números podemos buscar los números mayor y menor en la lista con la función max y min.
numbers=[1,2,100.01,90.45,3,4,5]
print(numbers)
print("Mayor:",max(numbers))
print("Menor:",min(numbers))

#Podemos también eliminar un elemento de la lista o eliminar la lista con el método o función del.
print(mix)
del mix[-1]
print(mix)
del mix[:2]
print(mix)
del mix

#Método slice. 
# Si decido agregar una lista a en una variable b, lo que estoy haciendo es apuntar al espacio
#en memoria de la lista a en la b, esoty quiere decir que toda modificación que haga en la lista a
#se va a ver reflejada en la lista b.
a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(a)
print(b)
#Para saber el espacio en memoria de ambas variables usamos el método id
print(id(a))
print(id(b))
#Para copiar la lista y que esta tenga su propio esapcio en memoria usamos el método slice.
#usando el método .copy() o a[:]
c = a.copy()
print(a)
print(b)
print(c)
print("Esp memoria lista a:", id(a))
print("Esp memoria lista b:", id(b))
print("Esp memoria lista c:", id(c))
#Agregamos un elemento a la lista y validamos los resultados.
a.append(6)
print(a)
print(b)
print(c)

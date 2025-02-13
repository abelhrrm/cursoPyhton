#las estructuras condicionales permiten evaluar condiciones para que determinan una acción en base a si
#esta condición es verdadera o falsa.
x = 10
if x > 5:
    print("x es mayor que 5")

#cuando la condición no se cumple podemos usar else para cumplir una acción

x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor que 5")

#Cuando tenemos una tercera opción.

x = 5
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual que 5")
else:
    print("x es menor que 5")

#Cuando debemos evaluar mas de una condición
#and requiere que las dos condiciones sean verdaderas

x = 16
y = 20

if x > 15 and y > 25:
    print("x es mayor que 15 y Y es mayor que 25")
else:
    print("x no es mayor que 15 o Y no es mayor que 25")

#or requiere que una de las dos condiciones sea verdadera

x = 16
y = 20

if x > 15 or y > 25:
    print("x es mayor que 15 o Y es mayor que 25")
else:
    print("x no es mayor que 15 y Y no es mayor que 25")

#if anidados que son if dentro de otros if

is_member = False
age = 15

if is_member:
    if age >= 15:
        print ("Tiene acceso eres miembro y tu edad es mayor o igual a 15 años")
    else:
        print ("NO tiene acceso eres miembro pero tu edad no es mayor o igual a 15 años")
else:
    print ("No Tiene acceso porque no eres miembro")

#juego de piedra papel o tijera

jugador1 = input ("jugador 1 escoge piedra, papel o tijera= ").lower() 
jugador2 = input ("jugador 2 escoge piedra, papel o tijera= ").lower()

if (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print ("Gana jugador 1")
elif (jugador1 == "piedra" and jugador2 == "piedra") or (jugador1 == "papel" and jugador2 == "papel") or (jugador1 == "tijera" and jugador2 == "tijera"):
    print("No ganda ningún jugador")
else: 
    print("Gana jugador 2")

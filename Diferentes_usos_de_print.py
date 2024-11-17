#1. Uso básico de print
print("Nunca pares de aprender")

#2. Uso de la coma en print
print("Nunca", "pares", "de", "aprender","con","comas")

#Con el operador mas "+" no añade espacios.
print("Nunca" + "pares" + "de" + "aprender")

#Se añade espacio si explicitamente lo agregas.
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

#3. Uso de sep especifica entre comillas el tipo de separador.
print("Nunca", "pares", "de", "aprender", sep=", ")

#4. Uso de end agrega el seperador que determinimos y luego añade en la misma linea el siguiente print.
print("Nunca", "pares", end=" ")
print("de aprender")

#5. Impresión de variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#6. Uso de formato con f-strings anteponer una f para iniciar el formato.
print(f"Frase: {frase}, Autor: {author}")

#7. Uso de formato con format
print("Frase: {}, Autor: {}".format(frase, author))

#8. Impresión con formato específico
valor = 3.14159
print("Valor: {:.3f}".format(valor))

#9. Saltos de línea y caracteres especiales
print("Hola\nmundo")
#Caracteres especiales escaparlos con \
print('Hola soy \'Carli\'')
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")

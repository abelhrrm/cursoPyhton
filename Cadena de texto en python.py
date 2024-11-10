#creamos dos variables para saber el tipo 
name = "Abel" 
print(type(name)) 
print(name) 

#Los string se asocian con comillas dobles, simples o 3 comillas simples 
name_1 = 'Abel' 
print(name_1) 
print(type(name_1)) 

#Las comillas triple simples son sensibles a los saltos de línea. 
name_2 = '''Abel 
Herrera''' 
print(name_2) 

#Podemos con sultar la posición de un carácter en una cadena de texto 
name_3 = "Abel Herrera" 
print(name_3[0]) 
print(name_3[1]) 
print(name_3[2]) 
print(name_3[3]) 

#Si deseo consultar las últimas posiciones debo usar los numero negativos empezando por -1 
print(name_3[-1]) 
print(name_3[-2]) 
print(name_3[-3]) 

#Podemos realizar operaciones con las cadenas de texto: concatenación y repetición. 
#Concatenación es suma de texto. 
#Repeteción es repetir las veces que vamos  
name_4 = "Abel" 
last_name = "Herrera Montiel" 
print(name_4 + " " + last_name) 

#repetición o replicación se realiza con el asterisco. 
print(name_4*6)
#Tamaño de la cadena de texto se puede saber con la función len()
print(len(name_4))

#Hay funciones propias de los String que se llaman métodos que tienen una sistaxis distinta a las funciones.
name_5 = "ABEL"
last_name_5 = "  Herrera Montiel" 
print(name_5.lower())
print(last_name_5.upper())
print(last_name_5.strip()) #Elimina los espacios iniciales.
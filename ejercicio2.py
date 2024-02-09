from EJERCICIO1 import *
print ("Ingrese los datos que se pediran a continuación:")
alt = aleatorio(6,1 , 45)
print (alt)

nombre = validar_texto("Ingrese su nombre: ")
apellido = validar_texto("Ingrese su apellido: ")
numdni = regresa_secuencia("Ingrese su número de DNI: ")
numif = validar_rango("Ingrese numeros enteros diferentes en el rango de : ")

premio = 0
coincidencias = 0
for i in numif:
    if i in alt:
        premio+=10
        coincidencias+=1
        
print (f"{nombre} {apellido}, identificado con el número de DNI {numdni}, obtuvo {coincidencias} coincidencias, y su premio es de S/.{premio:.2f}.")
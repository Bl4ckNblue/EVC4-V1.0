from random import randint as rd
def aleatorio (n: int, a: int , b: int):
    num = []
    try:
        for i in range(n):
            num.append(rd(a,b))
    except TypeError:
        print ("Un parámetro no es válido ")
    return num


def validar_texto(n):
    while True:
        try:
            t = input(n)
            if not t.isalpha():
                raise ValueError ("No se ingresaron caracteres de texto")
            else:
                print ("Se ha ingresado correctamente")
                break
        except ValueError as valor:
            print (f"Error:{valor}")
    return (t)



def regresa_secuencia (n):
    secuencia = []
    while True:
        try:
            Num = input(n)
            if Num.isdigit():
                for i in Num:
                    secuencia.append(i)
                break
            else:
                raise ValueError ("No se ingresaron caracteres numericos")
        except ValueError as digito:
            print (f"Error: {digito}")
    return "".join(secuencia)



def validar_rango (t: str):
    n = int(input("Ingrese la cantidad de números a generar: "))
    a = int(input("Ingrese el rango inicial: "))
    b = int(input("Ingrese el rango final: "))
    lista = []
    contador = 0
    while n != contador:
        try:
            Nuevo = input(t)
            if Nuevo.isalpha():
                print ("No debe ingresar letras")
            elif int(Nuevo) in lista:
                print ("Ingrese otro numero que no sea igual")
            elif a <= int(Nuevo) <= b:
                lista.append(int(Nuevo))
                contador+=1
            else:
                raise Exception ("Numero fuera de rango")
        except Exception as fuera:
            print (f"Error: {fuera}")

    return lista



        
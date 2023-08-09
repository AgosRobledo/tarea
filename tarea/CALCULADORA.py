#crear en un nuevo archivo .py todas las funciones pertinentes al funcionamiento de una calculadora. Entre ellas puedo mencionarles rápidamente : 
#sumar
#restar
#multiplicar
#dividir
#potencia
#radicación
import os
from fractions import Fraction
salir=False

def cantnum(mjs):
    while True:
        try:
            cant=int(input(mjs))
            if cant<100 and cant>0:
                return cant
            elif cant>=100 or cant<=0:
                print ("La cantidad ingresada es incorrecta ")
        except ValueError:
            print("La cantidad ingresada es invalidad ")

def suma ():
    cont=0
    num=[]
    cant=cantnum("Ingrese la cantidad de números que desea sumar: ")
    while cont<cant:
        numero = float(input("Ingrese el número {}: ".format(cont+1)))
        num.append(numero)
        cont+=1
    suma_string= "+".join(str(n) for n in num)
    resultado=sum(num)
    print("{} = {}".format(suma_string, resultado))
#En la línea 32 ustilice suma_string y join para mostrar los números ingresados por el usuario separado por el símbolo elegido "+".

def resta ():
    cont=0
    num=[]
    cant=cantnum("Ingrese la cantidad de números que desea restar: ")
    while cont<cant:
        numero = float(input("Ingrese el número {}: ".format(cont+1)))
        num.append(numero)
        cont+=1
    resta_string= "-".join(str(n) for n in num)
    resultado= num[0] - sum(num[1:]) 
    #acá num[0] es el número a restar y sum(num[1:] es la summa de los numero que se desean restar)
    print("{} = {}".format(resta_string, resultado))

def multiplicar ():
    cont=0
    num=[]
    cant=cantnum("Ingrese la cantidad de números que desea multiplicar: ")
    while cont<cant:
        numero = float(input("Ingrese el número {}: ".format(cont+1)))
        num.append(numero)
        cont+=1
    multiplicar_string= "-".join(str(n) for n in num)
    resultado= 1
    for n in num:
        resultado *=n 
    print("{} = {}".format(multiplicar_string, resultado))

def dividir (dividendo, divisor):
    if divisor==0:
        print ("No es posible dividir entre 0")
    else:
        return dividendo/divisor
    
def potencia (base, exponente):
    resultado= base ** exponente  #** es para elevar
    return resultado

def radiacion (radicando, indice):
    raiz= radicando ** (1/indice)
    return raiz 




while (salir==False):
    print (""" Bienbenido al menú de esta calculadora:
1)Suma
2)Resta
3)Multiplicar
4)Dividir
5)Potencia
6)Potencia
7)Salir
    """)
    opcion = int(input("Ingrese la operación que desea realizar "))
    os.system("cls")
    if opcion==1:
        suma()
        continuar = input("Ingrese ENTER para continuar ")
        os.system("cls")
    if opcion==2:
        resta ()
        continuar = input("Ingrese ENTER para continuar ")
        os.system("cls")
    if opcion==3:
        multiplicar ()
        continuar = input("Ingrese ENTER para continuar ")
        os.system("cls")
    if opcion==4:
        dividendo=float(input("Ingrese el número dividendo "))
        divisor=float(input("Ingrese el número divisor "))
        resultado=dividir(dividendo, divisor)
        print ("{} / {} = {}".format(dividendo, divisor, resultado))
        continuar = input("Ingrese ENTER para continuar ")
        os.system("cls")
    if opcion == 5:
        base=float(input("Ingrese la base "))
        exponente=float(input("Ingrese el exponente "))
        resultado=potencia(base, exponente)
        print("{} ** {} = {}".format(base, exponente, resultado))
        continuar = input("Ingrese ENTER para continuar ")
        os.system("cls")
    if opcion == 6:
        radicando=float(input("Ingrese el radicando "))
        indice= float(input("Ingrese el índice "))
        resultado=radiacion(radicando, indice)
        print("{} ** (1/{}) = {}". format(radicando, indice, resultado))
        continuar = input("Ingrese ENTER para continuar ")
        os.system("cls")
    if opcion == 7:
        opcion=input("¿Desea continuar? Si/No   ").upper()
        if opcion == "NO":
            print("♥ Gracias por usar esta calculadora ♥ ")
            break
        elif opcion == "SI":
            os.system("cls")
        else:
            print("Opción incorrecta")
            continuar = input("Ingrese ENTER para continuar ")
            os.system("cls")




        
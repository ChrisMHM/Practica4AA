import random
import os

#El algoritmo para base 10
def multiplicacion10(x, y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		potMedia = n / 2
		
		a = x / 10**(potMedia)
		b = x % 10**(potMedia)
		c = y / 10**(potMedia)
		d = y % 10**(potMedia)
		
		ac = multiplicacion10(a, c)
		bd = multiplicacion10(b, d)
		ad_mas_bc = multiplicacion10(a+b,c+d) - ac - bd
        
        #Modificacion para numeros de longitud impar
		prod = ac * 10**(2*potMedia) + (ad_mas_bc * 10**potMedia) + bd

		return prod
    
#El algoritmo para base 2
def multiplicacion2(x, y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		potMedia = n / 2
		
		a = x / 2**(potMedia)
		b = x % 2**(potMedia)
		c = y / 2**(potMedia)
		d = y % 2**(potMedia)
		
		ac = multiplicacion2(a, c)
		bd = multiplicacion2(b, d)
		ad_mas_bc = multiplicacion2(a+b,c+d) - ac - bd
        
        #Modificacion para numeros de longitud impar
		prod = ac * 2**(2*potMedia) + (ad_mas_bc * 2**potMedia) + bd

		return prod

#Genera numeros de n cifras considerando la base 2 para los limites superior e inferior
def n2Cifras(n):
    a = 1
    s = 0
    for i in range(1, n+1):
        if i%2 == 1:
            s = s + (1*(2**(n-a)))
            #print(s, a)
            a = a+1
        else:
            s = s + (0*(2**(n-a)))
            #print(s, a)
            a = a+1
    return s

def n10Cifras(n):
    a = 1
    s = 0
    for i in range(1, n+1):
        s = s + (i*(10**(n-a)))
        #print(s, a)
        a = a+1
    return s

respuesta = 1

while respuesta != 0:
    os.system('cls')
    print("Ingresa la base que con la que desea trabajar: ")
    print("Base 2, ingrese 2")
    print("Base 10, ingrese 10")
    base = input()

    if base==2:
        os.system('cls')
        print("Base 2")
        A = input("Numero de cifras de A: ")
        B = input("Numero de cifras de B: ")

        if A < 0 or B < 0:
            print("Error")
        elif A == 0 or B == 0:
            print("AxB: " + str(0))
        else:
            x = n2Cifras(A)
            y = n2Cifras(B)

            print("Numero A binario: " + str(bin(x)))
            print("Numero B binario: " + str(bin(y)))

            #print("Numero A decimal: " + str(x))
            #print("Numero B decimal: " + str(y))

            multi = multiplicacion2(x, y)

            print("AxB en binario: " + str(bin(multi)))
            #print("AxB en decimal: " + str(multi))
    elif base == 10:
        os.system('cls')
        print("Base 10")
        A = input("Numero de cifras de A: ")
        B = input("Numero de cifras de B: ")

        if A < 0 or B < 0:
            print("Error")
        elif A == 0 or B == 0:
            print("AxB: " + str(0))
        else:
            x = n10Cifras(A)
            y = n10Cifras(B)

            print("Numero A: " + str(x))
            print("Numero B: " + str(y))

            multi = multiplicacion10(x, y)

            print("AxB: " + str(multi))
    else:
        print("Base no valida")
    
    respuesta = input("Calcular otro producto? (si = 1/no = 0): ")
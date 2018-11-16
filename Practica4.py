import random
import os
from math import ceil, floor

#El algoritmo se mantiene igual que para base 10
def multiplicacion(x, y, base):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		m = int(ceil(float(n)/2))

        x_Sup = int(floor(x/base**m))
        x_Inf = int(x%(base**m))

        y_Sup = int(floor(y/base**m))
        y_Inf = int(y%(base**m))

        a = multiplicacion(x_Sup, y_Sup, base)
        b = multiplicacion(x_Inf, y_Inf, base)
        c = multiplicacion(x_Sup + x_Inf, y_Sup + y_Inf, base) - a - b

        prod =  int(a*(base**(m*2)) + c*(base**m) + b)
		
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

            multi = multiplicacion(x, y, base)

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

            multi = multiplicacion(x, y, base)

            print("AxB: " + str(multi))
    else:
        print("Base no valida")
    
    respuesta = input("Calcular otro producto? (si = 1/no = 0): ")
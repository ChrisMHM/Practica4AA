import random
import os
from math import ceil, floor

#El algoritmo se mantiene igual que para base 10
def multiplicacion(x, y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		m = int(ceil(float(n)/2))

        x_Sup = int(floor(x/2**m))
        x_Inf = int(x%(2**m))

        y_Sup = int(floor(y/2**m))
        y_Inf = int(y%(2**m))

        a = multiplicacion(x_Sup, y_Sup)
        b = multiplicacion(x_Inf, y_Inf)
        c = multiplicacion(x_Sup + x_Inf, y_Sup + y_Inf) - a - b

        prod =  int(a*(2**(m*2)) + c*(2**m) + b)
		
        return prod

#Genera numeros de n cifras considerando la base 2 para los limites superior e inferior
def nCifras(n):
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


respuesta = 1

while respuesta != 0:
    os.system('cls')
    print("Base 2")
    A = input("Numero de cifras de A: ")
    B = input("Numero de cifras de B: ")

    if A < 0 or B < 0:
        print("Error")
    elif A == 0 or B == 0:
        print("AxB: " + str(0))
    else:
        x = nCifras(A)
        y = nCifras(B)

        print("Numero A binario: " + str(bin(x)))
        print("Numero B binario: " + str(bin(y)))

        print("Numero A decimal: " + str(x))
        print("Numero B decimal: " + str(y))

        multi = multiplicacion(x, y)

        print("AxB en binario: " + str(bin(multi)))
        print("AxB en decimal: " + str(multi))
    
    respuesta = input("Calcular otro producto? (si = 1/no = 0): ")
import random
import os

def multiplicacion(x, y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		potMedia = n / 2
		
		a = x / 10**(potMedia)
		b = x % 10**(potMedia)
		c = y / 10**(potMedia)
		d = y % 10**(potMedia)
		
		ac = multiplicacion(a, c)
		bd = multiplicacion(b, d)
		ad_mas_bc = multiplicacion(a+b,c+d) - ac - bd
        
        #Modificacion para numeros de longitud impar
		prod = ac * 10**(2*potMedia) + (ad_mas_bc * 10**potMedia) + bd

		return prod

#Genera numeros aleatorios de n cifras considerando limites superior e inferior de base 10
def nCifras(n):
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
    print("Base 10")
    A = input("Numero de cifras de A: ")
    B = input("Numero de cifras de B: ")

    if A < 0 or B < 0:
        print("Error")
    elif A == 0 or B == 0:
        print("AxB: " + str(0))
    else:
        x = nCifras(A)
        y = nCifras(B)

        print("Numero A: " + str(x))
        print("Numero B: " + str(y))

        multi = multiplicacion(x, y)

        print("AxB: " + str(multi))
    
    respuesta = input("Calcular otro producto? (si = 1/no = 0): ")
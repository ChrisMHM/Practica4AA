import random
import os

#El algoritmo se mantiene igual que para base 10
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

#Genera numeros de n cifras considerando la base 2 para los limites superior e inferior
def randomNCifras(n):
    inferior = 2**(n-1)
    superior = (2**n)-1
    return random.randint(inferior, superior)


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
        x = randomNCifras(A)
        y = randomNCifras(B)

        print("Numero A binario: " + str(bin(x)))
        print("Numero B binario: " + str(bin(y)))

        print("Numero A decimal: " + str(x))
        print("Numero B decimal: " + str(y))

        multi = multiplicacion(x, y)

        print("AxB en binario: " + str(bin(multi)))
        print("AxB en decimal: " + str(multi))
    
    respuesta = input("Calcular otro producto? (si = 1/no = 0): ")
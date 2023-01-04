# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:26:18 2022

@author: juan
"""
#ALCANCE
# =============================================================================
# actividad 1
# =============================================================================
def cuadrado(n):
    pep =5
    pepe ="3"
    dia =[2,3,4]
    print(locals())
    print(n**2)
cuadrado (2)
"""
a) con el locals mostrara la variable y su valor
b)si hay cambio ya que el locals muestra todas las variables y sus valores 
dentro de la funcion. 
""" 

# =============================================================================
# actividad 2
# =============================================================================
c=4

def cuadrado():
    
    global c
    c=c+1
    
    print(c**2)
    
cuadrado()

"""
b) no se puede modificar porque esta fuera de la funcion.
c) si quisiera modificarlo tengo que aplicar el comando global y alli recien 
   podre modificarla
"""





# =============================================================================
# actividad 3
# =============================================================================


frase = "Hola"
def f():
    frase = "Es un lindo dia"
    print(frase)
f()

"""
el codigo imprimira es un lindo dia, el alcance de la variable es local
"""
# =============================================================================
# actividad 4
# =============================================================================

x = 3
def f():
    y = x + 1
    print(x)
    def g():
        x = 1
        print(y)
        print(x)
    g()
f()
"""
El codigo imprimira 3,4,1. el alcance de las variables x es global, luego la y 
es local, y luego la ultima x es local
"""
#Archivos de Texto

# =============================================================================
# actividad 5
# =============================================================================

archivo=open("palabras.txt","w")
archivo.write("hola\n")
archivo.write("como\n ")
archivo.write("va\n")
archivo.write("soy\n")
archivo.write("juan\n")
archivo.write("nose\n")
archivo.write("que \n")
archivo.write("mas \n")
archivo.write("poner\n")
archivo.write("listo\n")
archivo.close()

archivo=open("palabras.txt","r")
lineas=archivo.readlines()
a=len(lineas)
print(lineas,f"hay {a} lineas en el archivo")
# =============================================================================
# actividad 6
# =============================================================================

archivo=open("numeros.txt","w")
archivo.write("1\n")
archivo.write("2\n ")
archivo.write("3\n")
archivo.write("4\n")
archivo.write("5\n")
archivo.write("5\n")
archivo.write("9\n")
archivo.write("8 \n")
archivo.write("10\n")
archivo.write("10\n")
archivo.close()

# =============================================================================
# actividad 7
# =============================================================================

col=[]
archivo=open("colores.txt","w")
for i in range(5):
    a=input("escriba un color:")
    col.append(a)
    archivo.write(a)
    archivo.write("\n")
archivo.close()

print(col)

# =============================================================================
# actividad 8
# =============================================================================

with open("numeros.txt", "r") as archivo:
    lista = [int(linea) for linea in archivo] 
a=lista.count(5)
  
print(f"hay {a} veces el numero 5")



# =============================================================================
# actividad 9
# =============================================================================
with open("numeros.txt", "r") as archivo:
    lista = [int(linea) for linea in archivo]

print(lista)  
   
promedio=sum(lista)/len(lista)  
suma=sum(lista) 
print(f"el promedio es {promedio}, y la suma es {suma} ")

   


# =============================================================================
# actividad 10
# =============================================================================
import random

arch=open ("numerosjuan.txt","w")
for i in range(250):
    b=str(random.randint(1,100))
    arch.write(b)
    arch.write("\n")
arch.close()





# =============================================================================
# actividad 11
# =============================================================================
import random
a=input("defina nombre del archivo:")
intervalo1=int(input("defina un numero:"))
intervalo2=int(input("defina un numero mayor al anterior:"))

arch=open (a,"w")
for i in range(250):
    b=str(random.randint(intervalo1,intervalo2))
    arch.write(b)
    arch.write("\n")
arch.close()




# =============================================================================
# actividad 12
# =============================================================================


alto=int(input("defina altura:"))

for i in range(1):
    for i in range(alto):
        print("*",end=" ")
    print()

for i in range(alto - 2):
    print("* ", end="")
    for j in range(alto - 2):
        print("  ", end="")
    print("*")
    
for i in range(1):
    for i in range(alto):
        print("*",end=" ")
    print()   




# =============================================================================
# actividad 13
# =============================================================================

    


def binario(a):
    bina=""
    while True:
        if a>0:      
            d=a%2
            bina=bina+str(d)
            a=int(a/2)
        else:
            break
    return bina[::-1]

a = int(input("Ingresa un número decimal: "))

print(binario(a))

# =============================================================================
# actividad 14
# =============================================================================

def octal(d):
    octal = ""
    while d> 0:
        residuo = d % 8
        octal = str(residuo) + octal
        d = int(d / 8)
    return octal


a = int(input("Ingresa un número decimal: "))
b=int(input("Ingresa la base a la que deseas cambiarlo 2 o 8: "))
if b==2:
    print(binario(a))
else:
    print(octal(a))

# =============================================================================
# actividad 15
# =============================================================================

def decimal(a):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(a[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

a = input("Ingresa u numero binario: ")
print(decimal(a))


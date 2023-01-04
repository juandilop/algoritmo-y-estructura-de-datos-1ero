# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:12:15 2022

@author: juan lopez
"""
# =============================================================================
# Actividad 1
# =============================================================================
a=input("ingrese su nombre y apellido:")
print(a.title())


# =============================================================================
# Actividad 2
# =============================================================================
a=str(input("ingrese una frase:"))
b=len(a)
for caracter in range(b):
    if (caracter%2)==0:
      print(a[caracter])
      
# =============================================================================
# Actividad 3
# =============================================================================


a=input("ingrese una frase:")
b=input("ingrese una letra que quiera contar:")
print(a.count(b))

# =============================================================================
# Actividad 4
# =============================================================================
frase=input("Introduzca una frase:")
espacios=frase.count(" ")
for i in frase:
    if i.isalpha()==True or i==" " or i.isnumeric()==True:
        frase=frase.replace(i,"")
print("La frase introducida tiene {espacios} espacios.")
print("Los simbolos que se encuentran en ella son:",{frase})

# =============================================================================
# Actividad 5
# =============================================================================

nombre_archivo = input("ingrese nombre de archivo: " )
nombre_archivo_modificado  =""

for caracter in nombre_archivo:
    if caracter == "a":
        nombre_archivo_modificado = nombre_archivo_modificado + "4"
    if caracter == "e":
        nombre_archivo_modificado = nombre_archivo_modificado + "3"
    if caracter != "a" and caracter != "e":
        nombre_archivo_modificado = nombre_archivo_modificado + caracter

print(nombre_archivo_modificado)

# =============================================================================
# Actividad 6
# =============================================================================

nombre_archivo = input("ingrese nombre de archivo: " )
nombre_archivo_modificado  =""

for caracter in nombre_archivo:
    if caracter == " ":
        nombre_archivo_modificado = nombre_archivo_modificado + "_"
    if caracter == ".":
        nombre_archivo_modificado = nombre_archivo_modificado + ".***"
        break
    if caracter != " " and caracter != ".":
        nombre_archivo_modificado = nombre_archivo_modificado + caracter
print(nombre_archivo_modificado)

# =============================================================================
# Actividad 7
# =============================================================================

a= input("ingrese un numero de un solo digito: " )
flag=True
list_num=["cero","uno","dos","tres","cuatro","cuatro","cinco","seis","siete","ocho","nueve"]
for caracter in a:
    if a not in "123456789":
        flag=False
        
    if flag==True and len(a)==1:    
        a=int(a)
        print(list_num[a])
    else:
        print("dato erroneo")

# =============================================================================
# Actividad 8
# =============================================================================

a = input("Introduce una frase: ")
b=""
for caracter in a:
    if caracter != " " :   
        print(caracter,end="")
    else:
        print()
 
# =============================================================================
# actividad 9
# =============================================================================

lista_nombres=["juan","tomas","joaquin", "lisandro"," agustin"]

a = input("Introduce tu nombre: ")

b= a in lista_nombres 
if b==True:
    
    print("estas en la lista")
else:
    print("no estas en la lista")


# =============================================================================
# actividad 10
# =============================================================================


nombres=[]
nombresm=[]
for i in range (8):
    m=input("ingrese un nombre:").lower()
    nombres.append(m)

a0=(nombres[0][0])
a1=(nombres[1][0])
a2=(nombres[2][0])
a3=(nombres[3][0])
a4=(nombres[4][0])
a5=(nombres[5][0])
a6=(nombres[6][0])
a7=(nombres[7][0])

if a0=="m":  
    nombresm.append(nombres[0])
if a1=="m":  
    nombresm.append(nombres[1])
if a2=="m":  
    nombresm.append(nombres[2])    
if a3=="m":  
    nombresm.append(nombres[3])
if a4=="m":  
    nombresm.append(nombres[4])
if a5=="m":  
    nombresm.append(nombres[5])    
if a6=="m":  
    nombresm.append(nombres[6])
if a7=="m":  
    nombresm.append(nombres[7])     
print(nombresm)
    


# =============================================================================
# actividad 11
# =============================================================================


a = input("Introduce una frase: ")
b= a.split()
print(b)


# =============================================================================
# actividad 12
# =============================================================================

a = input("Introduce una frase: ")
b=list(a)
print(b)

# =============================================================================
# actividad 13
# =============================================================================

nombres=[]
apellidos=[]
nombresApellido=input("Introduzca un nombre y apellido:")
espacio=nombresApellido.find(" ")
nombres.append(nombresApellido[:espacio])
apellidos.append(nombresApellido[espacio+1:])
print(nombres)
print(apellidos)

# =============================================================================
# actividad 14 
# =============================================================================
c=0

for a in range(7):
    b =int( input("Introduce su nota: "))
    c=c+b
    
d=c/8 
e=round(d, 2)   
print(e)    

# =============================================================================
# actividad 15
# =============================================================================

a = input("Introduce una frase: ")
#sin lista
b=len(a)
print(b)
#con lista
palabras=[]
frase=input("Introduzca una frase:")
palabras=frase.split()
cantPalabras=len(palabras)
print("La frase tiene",cantPalabras," palabras.")

# =============================================================================
# actividad 16
# =============================================================================
listaNumero=[]
listaDigito=[]
while len(listaNumero)<5:
    listaNumero.append(input("Introduzca un numero de una o mas cifras:"))
for i in listaNumero:
    a=len(i)
    listaDigito.append(a)
print("La lista de numeros ingresados es:",listaNumero)
print("Los digitos que contiene cada numero son:",listaDigito)

# =============================================================================
# actividad 17
# =============================================================================
import random
a=0
for i in range(20):
    n=random.randint(1,6)
    print(n)
    a=a+n
b=a/20
print("el promedio de las 20 tiradas de dados es", b)
# =============================================================================
# actividad 18
# =============================================================================

a=0
for i in range(2500):
    n=random.randint(1,6)
    print(n)
    a=a+n
c=a/2500
print("el promedio de las 2500 tiradas de dados es", c," y el promedio de las 20 tiradas de dados es", b)
"""la diferencia que es que el promedio de las 2500 es mayor ya que hay muchas 
mas tiradas"""

# =============================================================================
# actividad 19
# =============================================================================
marca=[]

for i in range(10):
    n = input("Introduce una marca: ")
    marca.append(n)
        
n = random.randint(0, 10)    
print("la marca elegida es", marca[n])

# =============================================================================
# actividad 20
# =============================================================================
notas=[]
a =int( input("Introduce la cantidad de notas: "))

for i in range(a):
    n = input("Introduce una nota: ")
    notas.append(n)
    
print(notas)


# =============================================================================
# actividad 21
# =============================================================================

n=int(input("Introduzca un valor de n para la siguiente operacion ´1/1 + 1/2 +... 1/n´:"))
valores=[]
operacion=0
valores.append(1/n)
while n>1:
    n=n-1
    valores.append(1/n)
for i in valores:
    operacion=operacion+i
print("el resultado final de la operacion es ", round(operacion,3) )
# =============================================================================
# actividad 22
# =============================================================================
a =int( input("Introduce el numero para realizar la cuenta regresiva: "))
b=""
for i in range(a+1):
    b=a-i
    print(b)
#con while
a =int( input("Introduce el numero para realizar la cuenta regresiva: "))
b=""
while a>=0:
    print(a)
    a-=1
        
# =============================================================================
# actividad 23
# =============================================================================

numeros=[]
numeros_positivos=[]
numeros_negativos=[]
for i in range(10):
    a =int( input("Introduce un numero positivo o negativo: "))
    numeros.append(a)
for i in numeros:
    if i>0:
        numeros_positivos.append(i)
    else:
        numeros_negativos.append(i)
print("los numeros negativos son: ",numeros_negativos)
print("los numero positivos son: ",numeros_positivos)

# =============================================================================
# actividad 24
# =============================================================================
num=[]


while True :
    m=input("ingrese un numero o ingrese s para salir:")
    
    if m!="s":
        num.append(int(m))
    else:
        print("el codigo ha terminado")
        break

print("los numeros ingresados son:", num)
# =============================================================================
# actividad 25
# =============================================================================
num_par=[]
c=0
a =int( input("Introduce la cantidad de numeros que va a ingresar: "))
if a >99:
    a==99
for i in range(a):
    b=int(input("Introduzca un nuevo numero par:"))
    if b %2==0:
      num_par.append(b)
    elif b%2!=1:
        break
        print("se ingreso un numero impar ",b )
for i in num_par:
    c+=i
print("la suma de los numeros pares ingresados es:",c)
print("los numeros ingresados fueron:", num_par)
        

# =============================================================================
# actividad 26
# =============================================================================

numeros=[]
for i in range(10):
    a =int( input("Introduce un numero: "))
    numeros.append(a)
a=sorted(numeros)    
print("los numeros ordenados de menor a mayor estaran a continuacion ",a,a[9])

# =============================================================================
# actividad 27
# =============================================================================

a =int( input("Introduce un numero de 6 cifras: "))
c6=a%10
c5=int((a%100)/10)
c4=int((a%1000)/100)
c3=int((a%10000)/1000)
c2=int((a%100000)/10000)
c1=int((a%1000000)/100000)
print("su numero invertido es",str(c6)+str(c5)+str(c4)+str(c3)+str(c2)+str(c1))
# =============================================================================
# actividad 28
# =============================================================================
import random

a =int( input("Introduce un numero: "))
b =int( input("Introduce un numero mayor que el anterior: "))
while a>=b and a!=b:
    b=int(input("Por favor introduzca un nuevo valor de b, siendo b>a:"))
intervalo=[a]
print(intervalo)
while intervalo[-1]!=b:
    a+=1
    intervalo.append(a)
print(f"El intervalo [a,b] es: {intervalo}")
juego=random.choice(intervalo)
vidas=10
persona=int(input("Trata de adivinar el numero que eligio la computadora:"))
while True:
    if persona!=juego:
        vidas-=1
        if vidas!=0:
            persona=int(input(f"Perdiste una vida, te quedan {vidas}.\nIntenta de nuevo:"))
        else:
            print("Te quedaste sin vidas,pucha. El numero era:", juego)
            break
    else:
        print("Acertaste! el numero era", juego )
        break



# =============================================================================
# actividad 29
# =============================================================================

base=int(input("Introduzca la longitud de la base de la piramide:"))
while base%2==0 or base==1 or base==0:
    base=int(input("Introduzca un valor valido para la base (impar, distinto de 0 y 1):"))
lista=[]
for i in range(0,int(base/2+1/2)):
    a=int((base/2-1/2)-i)*" "+int(i+1)*"#"+i*"#"
    lista.append(a)
for i in lista:
    print(i)

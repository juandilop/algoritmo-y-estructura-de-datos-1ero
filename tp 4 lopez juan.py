# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:53:32 2022

@author: juan
"""
# =============================================================================
# actividad 1
# =============================================================================
def cuadrado(a):
    
    c=a**2
    return c

for i in range(5):
    a=int(input("ingrese un numero:"))
    print(cuadrado(a))

# =============================================================================
# acividad 2
# =============================================================================

def es_positivo(a):
    if a>0:
        return True
    else:
        return False
    
a=int(input("ingrese un numero:"))
print(es_positivo(a))

# =============================================================================
# actividad 3
# =============================================================================

def igual(a,b):
    if a==b:
        return True
    else:
        return False
 
    
a=input("ingrese un numero:")
b=input("ingrese un numero:")
print(igual(a, b))
# =============================================================================
# actividad 4
# =============================================================================
def signo(a):
    if a>0:
        return 1
    else:
        return -1


# =============================================================================
# actividad 5
# =============================================================================
def escalon(a):
    if a>0:
        return 1
    else:
        return 0



# =============================================================================
# actividad 6
# =============================================================================
def delta_de_dirac(a,b):
    if a==b:
        return 1
    else:
        return 0
    


# =============================================================================
# actividad 7
# =============================================================================

import math
def raiz(a,b,c):
    
    r=((-b + math.sqrt((b**2)-4*a*c))/(2*a))

      
    return r
a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
c=int(input("ingrese un numero:"))
print(raiz(a, b, c))

# =============================================================================
# actividad 8
# =============================================================================
def intervalo(n,a,b):
    if n>a and n<b:
       return True
    if n>b and n>a:
       return False
    else:
       return True

    
a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
n=int(input("ingrese un numero:"))
print(intervalo(n,a,b))

# =============================================================================
# actividad 9
# =============================================================================

def vocal(str):
    cont=0
    for caracter in a :
        if caracter in "aeiou"  :
            cont+=1
    return cont       
        
    
a=input("ingrese una frase:")
print(vocal(a))


# =============================================================================
# actividad 10
# =============================================================================
def temperatura(temp):
    f=((temp*(1.8)) + 32)
    return f

temp=int(input("ingrese la temperatura:"))
print(round(temperatura(temp),2),"°f")


# =============================================================================
# actividad 11
# =============================================================================
def concatenar(a,b):
  
    return (a+(" ")+b)

a=input("ingrese un numero:")
b=input("ingrese un numero:")
print(concatenar(a, b))

# =============================================================================
# actividad 12
# =============================================================================
def concatenar_1(a,b,c):
    if n==0:
        return a+b
    else:
        return a+("")+b

a=input("ingrese un numero:")
b=input("ingrese un numero:")
c=input("si desdea escribir todo junto presione 0,y si coloca 1 se escribira espaciado")
print(concatenar(a, b))

# =============================================================================
# actividad 13
# =============================================================================

def contador (a,b):
    cont=0
    for caracter in a :
        if b==caracter:
            cont+=1
    return cont      

a=input("ingrese un numero:")
b=input("ingrese un numero:")
print(contador(a, b))            


# =============================================================================
# actividad 14
# =============================================================================
def capitalizar(a):
    b=a[0].upper()
    for i in range(1,len(a)) :
       if b[i-1]=="":
           b=b+a[i].upper()
       else:
           b=b+a[i].lower()
    return b

a=input("ingrese un numero:")

print(capitalizar(a)) 

# =============================================================================
# actividad 15
# =============================================================================
def orden(a):
    c=sorted(a)
    return c
a=[]
for i in range(2) :
    b=int(input("ingrese un numero:"))
    a.append(b)
    
print(orden(a))


# =============================================================================
# actividad 16
# =============================================================================
def intervalo_par(a,b):
    c=0
    d=[]
    for i in range(a,b+1) :
       if i%2==0:
            c+=1  
            d.append(i)
    return c,d

a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))

print(f"lacnatidad de numeros pares dentro del intervalo elegido son:{intervalo_par(a,b)}, y estos son los numeros")






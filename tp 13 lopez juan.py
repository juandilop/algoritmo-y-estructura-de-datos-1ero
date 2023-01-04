# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:09:37 2022

@author: juan
"""

def secuencial(item,lista):
    n=len(lista)
    for i in range(n):
        if item==lista[i]:
            return i
    return -1



# =============================================================================
# actividad 1
# =============================================================================

import random
nros=[]
for i in range(10):
    n=random.randint(0, 20)
    nros.append(n)
    
buscar=int(input("ingrese el numero que desea buscar"))

pos=secuencial(buscar, nros)

if pos!=-1:
    print("el numero esta en la posicion",pos)
else:
    print("no esta en la lista ")


# =============================================================================
# actividad 2
# =============================================================================

alumnos=["pepe","raul","kike","pipo"]

buscar=input("ingrese el nombre que desea buscar: ")

pos=secuencial(buscar, alumnos)

if pos!=-1:
    print("el alumno se presento")
else:
    print("el alumno no se presento ")


# =============================================================================
# actividad 3
# =============================================================================


import random
nros=[]
for i in range(10):
    n=random.randint(0, 20)
    nros.append(n)
    
buscar=int(input("ingrese el numero que desea buscar: "))


def secuencial(item,lista):
    n=len(lista)
    lista2=[]
    for i in range(n):
        if item==lista[i]:
            lista2.append(i)
    if len(lista2)!=0:
        return lista2
    else:
        
        return -1

pos=secuencial(buscar,nros)

# =============================================================================
# actividad 4
# =============================================================================
import random
buscar=int(input("ingrese el numero: "))
buscar1=int(input("ingrese el numero mayor al anterior: "))

while buscar>buscar1:
    buscar=int(input("ingrese el numero de vuelta: "))
    buscar1=int(input("ingrese el numero mayor al anterior de nuevo: "))
    
lista=[]
cont=buscar
for i in range(buscar1-buscar+1):
    lista.append(cont)
    cont+=1
    
nros=int(input("ingrese el numero dentro del intervalo: "))

while nros<buscar or nros>buscar1 :    
    nros=int(input("ingrese el numero dentro del intervalo de nuevo: "))
    



while True:
    
    if buscar<=buscar1:
        medio=(buscar+buscar1)//2
        mid=input(f" {medio} Es este su numero?",)
        
        if mid=="igual":
            break
        elif mid=="mayor":
            buscar=medio+1
           
        elif mid=="menor":
            buscar1=medio-1
            
            
  
            
            
            
            
            
            

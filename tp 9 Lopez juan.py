# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:30:04 2022

@author: juan
"""
# =============================================================================
# actividad 1 
# =============================================================================
def factorial(n):
    if n==0:
        return 1
    if n!=0:
    
        a=n*factorial(n-1)
       
        return a
    
print(factorial(2597))


# =============================================================================
# actividad 2
# =============================================================================

def suma(n):
     if n==0:
         return 0
     if n!=0:
        a= n + suma(n-1)
        return a
    
    
print(suma(4))    
    
# =============================================================================
#  actividad 3   
# =============================================================================

def potencia (b,p):
    if p==0:
        return 1
    if p!=0:
        a= b* potencia(b,p-1)
        return a

print(potencia(2, 2598))

# =============================================================================
# actividad 4
# =============================================================================

def Fibonacci(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return (Fibonacci(Number-1)+Fibonacci(Number-2))
    

print(Fibonacci(8))


# =============================================================================
# actividad 5
# =============================================================================
def sumar1(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista [0]+sumar1(lista[1:])
    
listaNumeros = [1,2,3,4] 
print("Total Sumado: ", sumar1(listaNumeros))  

# =============================================================================
# actividad 6
# =============================================================================

def invertir (a):
    if len(a)==0:
        return ""
    else:
        return invertir(a[1:])+a[0]

n="hola como estas"
print(invertir(n))


# =============================================================================
# actividad 8
# =============================================================================

def pares (lista):
     listabool=[]
     if len(lista)==1:
         if (lista[0] % 2) ==0:
             listabool.append(True)
         else:
             listabool.append(False)
         return listabool
     else:
         listabool=pares(lista[1:])
         if lista[0]%2==0:
            listabool.append(True)
         else:
            listabool.append(False)
     return listabool
            
listaNumeros = [2,3,5,7,9,11] 
print(pares(listaNumeros)[::-1]) 


# =============================================================================
# actividad 9
# =============================================================================

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]      

lista=[1,2,3,4,9,6]

print(Max(lista))


# =============================================================================
# actividad 10
# =============================================================================

def Min(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Min(list[1:])
        return m if m < list[0] else list[0]      

lista=[1,2,3,4,9,6]

print(Min(lista))


# =============================================================================
# actividad 11
# =============================================================================

def gcd1(x, y):
    if(y==0):
        return x
    else:
        return gcd1(y,x%y)
    
print(gcd1(60,90))


# =============================================================================
# 
# =============================================================================

def cant_nombres(lista,letra):
    if len(lista)==1:
        if lista[0][0]==letra:
            return 1
        else:
            return 0
    else:
        return cant_nombres(lista[0:1], letra)+cant_nombres(lista[1:], letra)
a=["pepe","mria","mose"]

cant_nombres(a, "m")


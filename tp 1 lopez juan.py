# -*- coding: utf-8 -*-
import math
# =============================================================================
# actividad 1
# =============================================================================
print ("hola mundo")


# =============================================================================
# actividad 2
# =============================================================================
n=9

print(n)


# =============================================================================
# actividad 4
# =============================================================================

nom=input("ingrese su nombre:")
print("hola ", nom)

# =============================================================================
# actividad 4
# =============================================================================

a=int(input("ingrese su numero:"))
b=int(input("ingrese un numero:"))

print("se ingresaron los valores ", b,a )

# =============================================================================
# actividad 5
# =============================================================================
c=input("ingrese un numero:")
print("has introducido ",c, "gracias")

# =============================================================================
# actividad 6
# =============================================================================

d=int(input("ingrese su numero:"))
e=int(input("ingrese un numero:"))
suma=d+e
resta=d-e
division=d/e
multiplicacion=d*e
print("la suma es ",suma)
print("la resta es ",resta)
print("la multiplicacion es ",multiplicacion)
print("la division es", division)

# =============================================================================
# actividad 7
# =============================================================================

a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
n=int(input("ingrese un numero:"))
x=int(input("ingrese un numero:"))
y=int(input("ingrese un numero:"))
print("a)", 5*a+b)
print("b)", b**2)
print("c)", ((2*n)-1)/((2*n)+1))
print("d)",1*math.sqrt(n))
print("e)",2*x-y)
print("f)",(x-y)/(x+y))

# =============================================================================
# actividad 8
# =============================================================================

a=float(input("ingrese un numero real:"))
b=float(input("ingrese un numero real:"))
c=a/b
d=round(c,2)
print("el resultado de dividir",a,"y",b, "es ",d)

# =============================================================================
# actividad 9
# =============================================================================

a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
if a==b:
    print("iguales")
else:
    print("distintos")

# =============================================================================
# actividad 10
# =============================================================================


a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
if a<b:
    print("el numero mayor es", b)
else : 
    print("el mayor valor es ", a)   
        
# =============================================================================
# actividad 11
# =============================================================================

dolar=200.54
a=int(input("ingrese los dolares que desea cambiar:"))
b=a*dolar
c=b+(b*4/100)
d=round(c,2)
print("el valor de la transacción es de ", d)
 
# =============================================================================
# actividad 12
# =============================================================================

f=input("ingrese una frase:")
n=len(f)
print("la frase tiene",n,"caracteres" )


# =============================================================================
# actividad 13
# =============================================================================

a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
if a<b:
    print("el numero mayor es", b)
if a>b:
    print("el numero mayor es", a)
if a==b:
    print("son iguales")
    
    
# =============================================================================
# actividad 14
# =============================================================================

a=int(input("ingrese un numero:"))

if a<0:
    b=a*-1
    print(b)
else:
    print(a)

 
# =============================================================================
# actividad 15
# =============================================================================

f=input("ingrese una frase:")
n=len(f)
g=input("ingrese una otra frase:")
h=len(g)
if n==h:
    print("iguales")
if n<h:
    print("la frase ",g," tiene mas caracteres")
if n>h:
    print("la frase ",f," tiene mas caracteres")

 
# =============================================================================
# actividad 16
# =============================================================================

a=int(input("ingrese un numero:"))

if a<0:
    print("valor negativo")
else:
    print("valor positivo")
    
  
# =============================================================================
# actividad 17
# =============================================================================
  
p=int(input("ingrese un numero:"))
l=int(input("ingrese un numero:"))
mv=p
if l>mv:
    
    mv=l
    print("", p,",",mv )
else:
    print("",l,",",mv)

    
# =============================================================================
# actividad 18
# =============================================================================
    
a=int(input("ingrese un numero"))
b=int(input("ingrese un numero"))
c=int(input("ingrese un numero"))
mv=0
med=0
mini=0
if a>b and a>c:
    mv=a
    if b>c:
      med=b
      mini=c
    else:
        med=c
        mini=b
      
elif b>a and b>c:
    mv=b
    if a>c:
      med=a
      mini=c
    else:
      med=c
      mini=a
else:
    mv=c
    if a>b:
      med=a
      mini=b
    else:
      med=b
      mini=a
print(mv,med,mini)
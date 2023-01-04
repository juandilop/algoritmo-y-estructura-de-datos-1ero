# -*- coding: utf-8 -*-
"""
1)Definiremos algoritmo como la especificación rigurosa de la secuencia de
pasos a realizar sobre un autómata para alcanzar un resultado deseado en un 
tiempo definido.

Definiremos programa como el conjunto de instrucciones u órdenes
ejecutables sobre una computadora, que permite cumplir con una
función específica (dichas órdenes están expresadas en un lenguaje de
programación concreto)
la diferenicia es que si bien ambos son una serie de instrucciones el algoritmo 
puede estar escrito en codigo o lenguaje natural, mientras que el programa 
solo puede estar escrito en lenguaje de programacion 

2)Número Entero (int), Número Decimal (float), Cadena de Texto (str), complex, 
diet, tuple. Python admite el tamaño que la maquina soporte.

3)
    •Números enteros definidos con la palabra clave int
    •Letras o caracteres definidos con la palabra clave char
    •Números reales o en coma flotante definidos con las palabras claves
    float o double

La diferencia es que el lenguaje c tiene un tamaño admitido para cada tipo 
de dato.

4)
    a) n = int(”3.41”) es incorrecto porque cuando queremos transformar el numero 
    en entero se encuentra con un texto.
    b) p = str(”hola”) es incorrecta porque ya es es un str.
    c) n = ”23” + str(12) es incorrecta porque no se realiza la suma, 
    solamente se junta los dos numeros
    d) k = str(10) + str(533) es incorrecta porque no se realiza la suma, 
    solamente se junta los dos numeros

5)
    a) 3 ∗ (23 – 7) + 186 Rta: 234
    b) (185 + 53)/2 + 5 Rta: 124
    c) (314 + 21 – 117)/2 Rta: 109
    d) 48 + 2 ∗ (5 + 58/2) + 68 Rta: 184

6)
Los Algoritmos son independientes del lenguaje, lo que significa que un
 algoritmo puede ser implementado usando lenguajes diferentes.
Los algoritmos deben ser descriptos con precisión y sin ambigüedades.

7)
    b) Una secuencia de pasos que se deben realizar para obtener un cierto resultado útil, en un tiempo finito.
    d) Una secuencia de acciones que se deben realizar para cocinar una torta. 

8)
    a) Número de días desde el inicio del año. int
    b) Tiempo transcurrido desde el inicio del año hasta hoy, en días. float
    c) El número serial de un celular o aparato electrónico. int
    d) La edad de tu mascota. int
    e) La cantidad actual total de habitantes de una ciudad. int
    f) El promedio temporal de habitantes en una ciudad. float
    g) Un número de teléfono. int
    h) Cantidad de intentos permitidos para ingresar la contraseña. Int

9) si el numero el numero lo dividimos y el resto da 0 el numero es par, en 
cambio si el resto da 1 el numero es impar.

11) El algoritmo que diseñe tiene 2 listas una donde en una ingresan todos
los nombres y en la otra ingresan los nombres que empiezan con m. Para pedir el
ingreso de los nombres utilizo un for y los archivo en la primer lista. luego 
extraigo la primer letra a una variable y luego esa letra la coloco en un if y
si es la letra m es igual a la de la variable guardo el nombre en una lista 
diferente a la anterior. 

13)
Ropa
Libros
Cubiertos
Hojas de tarea
Comida

14) Al tener 4 numeros a ordenar tenemos 24 posibilidades de orden diferente.
entonces creo 24 condicionales para poder cubrir todos los ordenes posibles.

"""

# =============================================================================
# actividad 10
# =============================================================================
a=int(input("ingrese un numero:"))
p=a%2
if p==0:
    print("numero par")
else:
    print("impar")
    
# =============================================================================
# actividad 12
# =============================================================================

a=input("ingrese mes:")
b=int(input("ingrese dia:"))
if a=="enero":
    if b<=20:
        print("capricornio")
    else:
        print("acuario")
        
if a=="febrero":
    if b<=20:
        print("acuario")
    else:
        print("piscis")
        
if a=="marzo":
    if b<=20:
        print("piscis")
    else:
        print("aries")
        
if a=="abril":
    if b<=20:
        print("aries")
    else:
        print("tauro")
        
if a=="mayo":
     if b<=20:
         print("tauro")
     else:
         print("geminis")
              
if a=="junio":
     if b<=20:
         print("geminis")
     else:
         print("cancer")
         
if a=="julio":
     if b<=20:
         print("cancer")
     else:
         print("leo")
         
if a=="agosto":
     if b<=20:
         print("leo")
     else:
         print("virgo")
         
if a=="septiembre":
     if b<=20:
         print("virgo")
     else:
         print("libra")
         
if a=="octubre":
     if b<=20:
         print("libra")
     else:
         print("escorpio")
         
if a=="noviembre":
     if b<=20:
         print("escorpio")
     else:
         print("sagitario")
         
if a=="diciembre":
     if b<=20:
         print("sagitario")
     else:
         print("capricornio")
# =============================================================================
# actividad 15
# =============================================================================

a=int(input("ingrese un numero"))
b=int(input("ingrese un numero"))
c=int(input("ingrese un numero"))
d=int(input("ingrese un numero"))

if a>b and b>c and c>d:
    print(a,b,c,d)
elif a>c and c>b and b>d:
        print(a,c,b,d)
elif a>c and c>d and d>b:
        print(a,c,d,b)
elif a>d and d>c and c>b:
        print(a,d,c,b)
elif a>d and d>b and b>c:
        print(a,d,b,c)
elif a>b and b>d and d>c:
        print(a,b,d,c)


elif b>a and a>c and c>d:
    print(b,a,c,d)
elif b>a and a>d and d>c:
    print(b,a,d,c)
elif b>c and c>a and a>d:
    print(b,c,a,b)
elif b>c and c>d and d>a:
    print(b,c,d,a)
elif b>d and d>c and c>a:
    print(b,d,c,a)
elif b>d and d>a and a>c:
    print(b,d,a,c)


elif c>a and a>b and b>d:
    print(c,a,b,d)
elif c>a and a>d and d>b:
    print(c,a,d,b)
elif c>b and b>a and a>d:
    print(c,b,a,b)
elif c>b and b>d and d>a:
    print(c,b,d,a)
elif c>d and d>b and b>a:
    print(c,d,b,a)
elif c>d and d>a and a>b:
    print(c,d,a,b)

elif d>a and a>b and b>c:
    print(d,a,b,c)
elif d>a and a>c and c>b:
    print(d,a,c,b)
elif d>b and b>a and a>c:
    print(d,b,a,c)
elif d>b and b>c and c>a:
    print(d,b,c,a)
elif d>c and c>b and b>a:
    print(d,c,b,a)
elif d>c and c>a and a>b:
    print(d,c,a,b)    
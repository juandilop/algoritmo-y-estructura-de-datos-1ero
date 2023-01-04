# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:05:49 2022

@author: juan
"""
def buble(v):
    n=len(v)
    for i in range(n):
        for j in range(n-i-1):
            if v[j]>v[j+1]:
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux
                
def insercion(v):
    n=len(v)
    for i in range (1,n):
        item=v[i]
        j=i-1
        while j>=0 and item<v[j]:
            v[j+1]=v[j]
            j=j-1
        v[j+1]=item
        
def seleccion(v):
    n=len(v)
    for i in range(n):
        min_pos=i
        for j in range(i+1,n):
            if v[j]<v[min_pos]:
                min_pos=j
        v[i],v[min_pos]=v[min_pos],v[i]
          
# =============================================================================
# actividad 1
# =============================================================================

lista=[76, 21, 34, 68, 31, 27, 53]

print(lista)


# =============================================================================
# actividad 2
# =============================================================================

l2=[6, 2, 4, 8, 3, 7, 5]

seleccion(l2)


# =============================================================================
# actividad 3
# =============================================================================

l3=[]
for i in range(6):
    a=int(input("ingrese un nro"))
    l3.append(a)
lbuble=l3.copy()
lisercion=l3.copy()
lseleccion=l3.copy()
    
    
         
print(lbuble)


print(lisercion)

print(lseleccion)



# =============================================================================
# actividad 4
# =============================================================================

import random
archivo=open("nro.txt","w")

for i in range(50):
    a=str(random.randint(0, 100))
    archivo.write(a)
    archivo.write("\n")
archivo.close()

archivo=open("nro.txt","r")
lineas=archivo.readlines()
archivo.close()
zz=[]
for i in range(50):
    a=int(lineas[i].strip("\n"))
    zz.append(a)
buble(zz)

archiv=open("ordenado.txt","w")
for i in range(50):
    archiv.write(str(zz[i]))
    archiv.write("\n")

archiv.close()


# =============================================================================
# actividad 5
# =============================================================================


import numpy as np
fam= [181.5, 72., 34.7, 171.3, 161.9]
arraycito= np.array(fam)


def seleccion(v):
    n=len(v)
    for i in range(n):
        min_pos=i
        for j in range(i+1,n):
            if v[j]<v[min_pos]:
                min_pos=j
        v[i],v[min_pos]=v[min_pos],v[i]

seleccion(arraycito)
print(arraycito)


"no hay diferencia"


# =============================================================================
# actividad 6
# =============================================================================

import numpy as np
m6=np.random.randint(100,size=(10))
m61=m6.copy()
m62=m6.copy()
m63=m6.copy()

seleccion(m6)
buble(m62)
insercion(m63)


# =============================================================================
# actividad 7
# =============================================================================x="mousze"

lista=["barco","casa","ala","aala"]

buble(lista)



# =============================================================================
# actividad 8
# =============================================================================


listaprecios=[]
for i in range(10):
    a=int(input("Escriba el precio de golosinas"))
    listaprecios.append(a)

listaprecios2=listaprecios.copy()

seleccion(listaprecios)
insercion(listaprecios2)


# =============================================================================
# actividad 9
# =============================================================================

import random
lista=[]

for i in range (6):
    x=random.randint(0,20)
    lista.append(x)
    
import numpy as np
v=np.random.randint(20,size=(6))

buble(lista)
seleccion(v)



# =============================================================================
# actividad 9
# =============================================================================

v=np.random.randint(20,size=(4,6))
v1=np.zeros(6,dtype="int32")
for i in range(4):
    for j in range(6):
        v1[j]=v[i,j]
        buble(v1)
        v[i,j]=v1[j]




# =============================================================================
# actividad 11
# =============================================================================

def secuencial(item,lista):
    n=len(lista)
    for i in range(n):
        if item==lista[i]:
            return i
    return -1
pacientes=open("pacientes.txt","w")
pacientes.write("Sanchez , Luis , 64, OSDE \n")
pacientes.write("Balaz , Sara , 32, OSECAD \n")
pacientes.write("Lipa , Julieta , 27, OSDE \n")
pacientes.write("Perez , Lucila , 30, OSECAD \n")
pacientes.close()

paciente=open("pacientes.txt","r")
personas=paciente.read()
paciente.close()

paciente=open("pacientes.txt","r")
personas1=paciente.readlines()
paciente.close()


pers=personas.split()
edades=[]
apellidos=[]
ape_ordenados=[]
for i in range(0,len(pers)):
    if len(pers[i])==3:
        if i %2==0:
            a=int(pers[i].strip(","))
            edades.append(a)
    if i%6==0 :
        apellidos.append(pers[i])

eda=edades.copy()
buble(edades)       
for i in range(4):
    a=secuencial(edades[i], eda)
    ape_ordenados.append(apellidos[a])

po=[]
pers2=pers.copy()
for i in range(len(ape_ordenados)):
    a=secuencial(ape_ordenados[i],pers2)
    for j in range(6):
        
        po.append(pers[a+j])
   
c=0
paciente=open("pacientes_ordenados.txt","w")
for i in range(len(personas1)):
    c=+6*i
    for j in range(6):
        paciente.write(po[c+j])
    
    paciente.write("\n")

        
paciente.close()


# =============================================================================
# actividad 12
# =============================================================================

import random
arch=open("libro.txt","w")
arch.write("""¿Por qué organizaciones que alguna vez fueron poderosas, como Singer, TWA, Pullman y FAO Schwarz, no
sobrevivieron la prueba del tiempo? ¿Por qué otras, como 3M, Apple, BMW y GE, no sólo soportan décadas de condiciones empresariales turbulentas, sino que prosperan y llegan a dominar sus respectivas industrias? Una explicación parcial de este éxito tiene que ver con la capacidad de estas compañías para
crear, mantener y modificar (cuando es necesario) su estructura organizacional con el fin de responder a
las cambiantes demandas de sus grupos de interés y sus ambientes externos. Algunos de los cambios
más dramáticos en las últimas dos décadas son el aumento en la hipercompetencia debido a la globalización, los rápidos avances en la tecnología y la desregulación a gran escala de industrias que alguna vez
estuvieron protegidas.
De este periodo de turbulencias, muchas compañías exitosas han surgido más fuertes y con más perspectivas que antes al modificar o reinventar su estructura organizacional. Tomemos como ejemplo el caso
de Sara Lee Corporation. Esta compañía de productos de consumo con valor de 15.9 mil millones de dólares, conocida por sus marcas Hillshire Farm, Jimmy Dean y Sara Lee, decidió modernizar la estructura
organizacional de su grupo de ventas de bebidas y alimentos, de modo que se fomentara una mayor atención a sus consumidores; para encabezar este esfuerzo, creó la posición de director en jefe de servicios al
consumidor, para que sus clientes de bebidas y alimentos se convirtieran en la principal fuerza impulsora
de esta división. ¿Qué cambios hicieron? Reemplazaron a los agentes, que anteriormente eran los intermediarios entre los vendedores de Sara Lee y los puntos de venta al menudeo como Wal-Mart y Safeway,
por su fuerza directa de ventas y esto permitió mayor contacto con los clientes; se contrataron nuevos
vendedores de compañías que estaban muy enfocadas en los consumidores, se formó una nueva estructura organizacional en la división de ventas y se realizaron cursos de capacitación sobre los consumidores.
Los resultados han sido positivos: tanto el volumen de ventas como la rentabilidad han mejorado desde
que se reorganizó la estructura. De modo similar, compañías como GE, 3M, Ericsson y Amgen que han
realizado exitosos ajustes a sus estructuras organizacionales para enfrentar los cambios en las condiciones del mercado, han obtenido los siguientes beneficios:""")
arch.close()


archivo=open("libro.txt","r")
contenido=archivo.readlines()
archivo.close()

contenido1=contenido.copy()
contsaca=[]
lista=[]

for i in range(len(contenido1)):
    a=contenido.pop(0)
    b=a.split()
    c=random.randint(0,len(b))
    contsaca.append(b[c])
    a=0
    b=0
    
    
buble(contsaca)    
    
# =============================================================================
# actividad 13
# =============================================================================



# =============================================================================
# actividad 14
# =============================================================================
notas=[]
for i in range(10):
    a=int(input("ingrese una nota"))
    notas.append(a)
    
buble(notas)

print(f"la notas mas baja fue {notas[0]}, y la mas alta fue {notas[-1]}")



# =============================================================================
# actividad 15
# =============================================================================


Desordenados =[ "Legolas", "Sam", "Frodo", "Sauron", "Gollum"]
cantidad=[]
Ordenados=[]

for i in range(len(Desordenados)):
    letras=len(Desordenados[i])
    cantidad.append(letras)
    
cant=cantidad.copy()   
buble(cantidad)


for i in range(len(Desordenados)):
    a=secuencial(cantidad[i], cant)
    zz=Desordenados.pop(a)
    cant.pop(a)
    Ordenados.append(zz)
print(Ordenados)



















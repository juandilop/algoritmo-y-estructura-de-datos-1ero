# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:53:17 2022

@author: juan
"""

# =============================================================================
# actividad 1
# =============================================================================

class pila:
    def __init__(self):
        self.items=[]
        
    def push (self,x):
       self.items.append(x)
    
    def peek(self):
        return self.items[-1]
       
    def esta_vacia(self):
        return self.items==[]
       
    def __len__(self):
        return len(self.items)
    
    def pop (self):
        if len(self.items)==0:
            return ("vacia")
        else:
            return self.items.pop()
pila1=pila()
pila1.push(3)
pila1.push(2)
pila1.push(1)
print(pila1)

pila2=pila()      
pila2.push(pila1.pop())
pila2.push(pila1.pop())
pila2.push(pila1.pop())        
        

# =============================================================================
# actividad 2
# =============================================================================

        
pila1=pila()
pila1.push("h")
pila1.push("o")
pila1.push("l")
pila1.push("a")
print(pila1)

pila2=pila()      
pila2.push(pila1.pop())
pila2.push(pila1.pop())
pila2.push(pila1.pop())      
pila2.push(pila1.pop())   

# =============================================================================
# actividad 3
# =============================================================================
n="seres"
pila1=pila()
pila2=pila()      

for i in range(len(n)):
    pila1.push(n[i])
    pila2.push(n[i])

for i in range(len(n)):
    contador=0
    a=pila1.peek()
    b=pila2.peek()
    if a==b:
        pila1.pop()
        pila2.pop()
        contador+=1
    while contador!=len(n):
        print()
    

# =============================================================================
# actividad 4
# =============================================================================

ciudades_ida=pila()
ciudades_ida1=pila()

ciudades_vuelta=pila()

c=int(input("ingrese por cuantas ciudades paso"))
for i in range(c):
    a=input("ingrese 3 ciudades por las que paso:")
    ciudades_ida.push(a)
    ciudades_ida1.push(a)

for i in range(c):
    ciudades_vuelta.push(ciudades_ida1.pop())

print(ciudades_ida,ciudades_vuelta)    
    

# =============================================================================
# actividad 5
# =============================================================================


cadenapila=pila()
parentesis1=pila()
parentesis2=pila()
corchete1=pila()
corchete2=pila()
cadena="([h]olas)"

for i in cadena:
    cadenapila.push(i)

for i in cadena:
    a=cadenapila.pop()
    if a=="[":
        corchete1.push(a)
    if a=="]":
        corchete2.push(a)
    if a=="(":
        parentesis1.push(a)
    if a==")":
        parentesis2.push(a)
        
c1=corchete1.__len__()

c2=corchete2.__len__()

p1=parentesis1.__len__()

p2=parentesis2.__len__()

if c1==c2 and p1==p2:
    print("equilibrado")
else:
    print("desequilibrado")


# =============================================================================
# actividad 6
# =============================================================================

contenedor=pila()
contenedorx=pila()
contenedorsacado=pila()

a=int(input("cuantos contenedores tiene"))
for i in range(a):
    contenedor.push(i)
contenedor_b=int(input("que contenedor queres sacar:"))
for i in range(a):
    b=contenedor.pop()
    if b==contenedor_b:
        contenedorsacado.push(b) 
        break
    else:
        contenedorx.push(b)
        
c2=contenedorx.__len__()
for i in range(c2):
    z=contenedorx.pop()
    contenedor.push(z)


# =============================================================================
# actividad 7
# =============================================================================

archivo1=pila()
archivo2=pila()

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
archivo.close()

for i in range(len(lineas)):
    a=lineas[i]
    archivo1.push(a)
    
archivof=open("palabrasf.txt","w")

for i in range(len(lineas)):
    x=archivo2.push(archivo1.pop())
    c=archivo2.peek()
    archivof.write(str(c))
archivof.close()


# =============================================================================
# actividad 8
# =============================================================================
cadenapila=pila()
body1=pila()
body2=pila()
center1=pila()
center2=pila()
h11=pila()
h12=pila()
p1=pila()
p2=pila()


archivo=open("html.txt","w")
archivo.write("<body>")
archivo.write("\n")
archivo.write("<center>")
archivo.write("\n")
archivo.write("<h1> El Poema del Anillo </h1>")
archivo.write("\n")
archivo.write("</center>")
archivo.write("\n")
archivo.write("""<p> Tres Anillos para los Reyes Elfos bajo el cielo,
Siete para los Señores Enanos en palacios de piedra,
Nueve para los Hombres Mortales condenados a morir,
Uno para el Se~nor Oscuro, sobre el trono oscuro
en la Tierra de Mordor donde se extienden las Sombras.
Un Anillo para gobernarlos a todos. Un Anillo para encontrarlos,
un Anillo para atraerlos a todos y atarlos en las tinieblas
en la Tierra de Mordor donde se extienden las Sombras. </p>""")
archivo.write("\n")
archivo.write("</body>")
archivo.close()


archivo=open("html.txt","r")
lineas=archivo.read()
archivo.close()
 
c=lineas.split()

for i in range(len(c)):
    cadenapila.push(c[i])


for i in range(len(cadenapila)):
    a=cadenapila.pop()
    if a=="<body>":
        body1.push(a)
    if a=="</body>":
        body2.push(a)
    if a=="<center>":
        center1.push(a)
    if a=="</center>":
        center2.push(a)
    if a=="<h1>":
        h11.push(a)
    if a=="</h1>":
        h12.push(a)
    if a=="<p>":
        p1.push(a)
    if a=="</p>":
        p2.push(a)
        

if body1.__len__()==body2.__len__() and center1.__len__()==center2.__len__() and h11.__len__()==h12.__len__() and p1.__len__()==p2.__len__():
    print("equilibrado")
else:
    print("desequilibrado")

# =============================================================================
# actividad 9
# =============================================================================

#polaca inversa (10 2 +)



stack =pila()
for i in range(2):
    
    a=int(input("ingrese el numero de posicion {i} numero: "))
    stack.push(a)
c=input("ingrese el operando: ")  



top1 = stack.pop()
top2 = stack.pop()
if c == '+':
    print(top2 + top1)
elif c == '-':
    print(top2 - top1)
elif c == '*':
    print(top2 * top1)
elif c == '/':
    print(int(top2 / top1))


# =============================================================================
# actividad 10
# =============================================================================

frase=pila()
a=input("ingrese una frase: ")
c=a.split()
for i in range(len(c)):
    frase.push(c[i])

for i in range(len(c)):
    p=frase.pop()
    print(p, end=" ")



# =============================================================================
# clase cola
# =============================================================================

class cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

# =============================================================================
# actividad 11
# =============================================================================

fila=cola()
obrasocial=[]
a=int(input("cuantos pacientes tiene: "))
for i in range(a):
    paciente=input("nombre del paciente : ")
    fila.agregar(paciente)

for i in range(a):
    p=fila.avanzar()
    obr=input(f"{p} tiene obra social?")
    obrasocial.append(obr)



# =============================================================================
# actividad 12
# =============================================================================

import random
filamix=cola()
filah=cola()
filam=cola()


for i in range (10):
    n=random.randint(1, 2)
    if n==1:
        n="hombre"
    if n==2:
        n="mujer"
    filamix.agregar(n)
        
for i in range(10):
    p=filamix.avanzar()
    if p=="hombre":
        filah.agregar(p)
    if p=="mujer":
        filam.agregar(p)


# =============================================================================
# actividad 13
# =============================================================================

filacorreo=cola()
for i in range (10):
    n=random.randint(1, 2)
    if n==1:
        n="hombre"
    if n==2:
        n="mujer"
    filacorreo.agregar(n)
    
for i in range (10):
        p=filacorreo.avanzar()
        co=int(input(f"{p} ¿cuantas cartas tiene para entregar?"))
        if co>=7:
            filacorreo.agregar(p)



















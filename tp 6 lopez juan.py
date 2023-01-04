# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:59:37 2022

@author: juan
"""



# =============================================================================
# actividad 1
# =============================================================================
import numpy as np
fam= [181.5, 72., 34.7, 171.3, 161.9]
arraycito= np.array(fam)

a=arraycito.dtype
b=arraycito.ndim
c=arraycito.shape
d=arraycito.size
print(a,b,c,d)

# =============================================================================
# actividad 2
# =============================================================================


m=np.zeros((2,4,3))
print(m)

# =============================================================================
# actividad 3
# =============================================================================


m1=np.random.random((4,6))
print(m1)

# =============================================================================
# actividad 4
# =============================================================================

"""no anda"""
m2=np.linspace(1, 6,25)
print(m2)



# =============================================================================
# actividad 5
# =============================================================================
lista=[]
for i in range(6):
    li=input("ingrese un numero:")
    lista.append(li)
    
m2=np.array(lista)
print(m2)

# =============================================================================
# actividad 6
# =============================================================================

m6=np.random.randint(5,size=(16))
print(m6)
for i in range(16):
        if m6[i]==0:
            m6[i]=-1
print (m6)
    

# =============================================================================
# actividad 7
# =============================================================================

lista=[1,2,3]
lista1=[2,3,4]
arr=np.ones(3)
a=lista+arr
b=lista+lista1
print(a,b)
"""la suma entre unalista y otra lista se juntan los numeros pero no se suman
en cambio al sumar una lista y un vector se suman los valores que ocupan la 
misma posicion"""

# =============================================================================
# actividad 8 
# =============================================================================
 
m8=np.zeros((3,3)) 
print(m8)    
for i in range(3):
    for j in range(3):
        
        m8[i,j]=i+i+i+j+1
print(m8)


# =============================================================================
# actividad 9
# =============================================================================


m9=np.random.randint(12,size=(16,20),dtype="int64")
print(m9)


# =============================================================================
# actividad 10
# =============================================================================

m10=np.random.randint(1,6,(5,6))
print(m10)
for i in range(5):
    for j in range(6):
        if i==4:
            m10[i,j]=0
print(m10)

# =============================================================================
# actividad 11
# =============================================================================

def suma_arrays(a,b):
    z=int(input("ingrese la dimension del array:"))
    for i in range(z):
        a[i]=a[i]+b[i]
    return a
    
arr1=np.ones(3)
arr2=np.ones(3)
print(suma_arrays(arr1, arr2))

# =============================================================================
# actividad 12
# =============================================================================
def prod_arrays(a,b):
    z=int(input("ingrese la dimension del array:"))
    for i in range(z):
        a[i]=a[i]*b[i]
    return a
    
arr1=np.ones(3)
arr2=np.ones(3)
print(prod_arrays(arr1, arr2))


# =============================================================================
# actividad 13
# =============================================================================

def sum_arrays(a,b):
    z=int(input("ingrese la cantidad de filas del array:"))
    x=int(input("ingrese la cantidad de filas del array:"))
    for i in range(z):
       for j in range(x):
           a[i,j]=a[i,j]+b[i,j]
    return a

m9=np.random.randint(5,size=(3,3))
m10=np.random.randint(5,size=(3,3))
   
print(m10,"\n",m9)
print(sum_arrays(m10,m9))

# =============================================================================
# actividad 14
# =============================================================================


m14=np.zeros((6,6)) 
   
for i in range(6):
    for j in range(6): 
        if i==j:
                m14[i,j]=1
         
print(m14)
 
# =============================================================================
# actividad 15
# =============================================================================

m14=np.zeros((6,6)) 
   
for i in range(6):
    for j in range(6): 
        if i%2==0:
            
            m14[i,j]=+1
print(m14)


# =============================================================================
# actividad 16
# =============================================================================

m14=np.zeros((6,6)) 
   
for i in range(6):
    for j in range(6): 
        if i%2==0:
            if j%2==0:
                
                m14[i,j]=+1
        else:
            if j%2==1:
               m14[i,j]=+1  
print(m14)




# =============================================================================
# actividad 17
# =============================================================================

pol=0
pp=[]
nombres=np.ndarray((4,3), dtype="<U4")

for i in range(4):
    for j in range(3): 
        a=input("ingrese un nombre:")
        nombres[i,j]=a
print(nombres)

for i in range(4):
    z=nombres[i,1][::-1]
    
    pp=list(z)
    
    if "s"== pp[0]:
        pol+=1
        
print(f"la cantidad de palabras terminadas con la letra s es {pol}")   
# =============================================================================
# actividad 17
# =============================================================================
import numpy as np
import math
archivo=open("notas.txt","w")
prom_linea=0
prom_total=0
prom_linea1=0
proms_lin_tot=[]
prom_alumno=0
prom_alumno1=[]
prom_alumno12=[]
nota=[]
notafin=[]
prom=0
alumnos=np.zeros((3,8)) 


for i in range (3):
    for j in range(8):
        a=int(input(f"ingrese la nota {i+1},del alumno {j+1}:"))
        alumnos[i,j]=a
        archivo.write(str(a))
        prom_linea=(prom_linea+a)
        prom_total+=a
        nota.append(a)
    nota.sort(reverse=True)
    x=nota[0]
    notafin.append(x)
    prom_linea1=(prom_linea-prom_linea1)/8
    proms_lin_tot.append(prom_linea1)
    prom_linea=0
    prom_linea1=0
    archivo.write("\n")
    nota.clear()
archivo.close() 
   
print(alumnos)
print("la nota promedio del primer examen fue", proms_lin_tot[0]," \n la del segundo fue" ,proms_lin_tot[1],"\n la del tercero fue",proms_lin_tot[2])
print("el promedio total de las notas fue ",prom_total/24)
print(f"la nota mas alta del examen 1 fue {notafin[0]},\nla nota mas alta del examen 2 fue {notafin[1]},\n la nota mas alta del examen 3 fue {notafin[2]}")


for j in range(8):
    for i in range(3):
        d=alumnos[i,j]
        prom_alumno+=d
        prom_alumno12.append(d)
    prom=prom_alumno/3
    z=round(prom,2)
    prom_alumno12.sort(reverse=True)
    print(f"el promedio del alumno {j+1} es {z}, y la nota mas alta fue {prom_alumno12[0]}, y \n la mas baja fue {prom_alumno12[2]} ")
    print(prom_alumno12)
    prom_alumno=0
    prom_alumno12.clear()
    prom_alumno1.clear()

# =============================================================================
# actividad 18
# =============================================================================


import numpy as np
import math
archivo=open("notas1.txt","w")
prom_linea=0
prom_total=0
prom_linea1=0
proms_lin_tot=[]
prom_alumno=0
prom_alumno1=[]
prom_alumno12=[]
nota=[]
notafin=[]
prom=0
alumnos=np.random.randint(1,10,(3,500)) 


for i in range (3):
    for j in range(500):
        
        al=alumnos[i,j]
        archivo.write(str(al))
        prom_linea=(prom_linea+al)
        prom_total+=al
        nota.append(al)
    nota.sort(reverse=True)
    x=nota[0]
    notafin.append(x)
    prom_linea1=(prom_linea-prom_linea1)/500
    proms_lin_tot.append(prom_linea1)
    prom_linea=0
    prom_linea1=0
    archivo.write("\n")
    nota.clear()
archivo.close() 
   
print(alumnos)
print("la nota promedio del primer examen fue", proms_lin_tot[0]," \n la del segundo fue" ,proms_lin_tot[1],"\n la del tercero fue",proms_lin_tot[2])
print("el promedio total de las notas fue ",prom_total/1500)
print(f"la nota mas alta del examen 1 fue {notafin[0]},\nla nota mas alta del examen 2 fue {notafin[1]},\n la nota mas alta del examen 3 fue {notafin[2]}")


for j in range(500):
    for i in range(3):
        d=alumnos[i,j]
        prom_alumno+=d
        prom_alumno12.append(d)
    prom=prom_alumno/3
    z=round(prom,2)
    prom_alumno12.sort(reverse=True)
    print(f"el promedio del alumno {j+1} es {z}, y la nota mas alta fue {prom_alumno12[0]}, y \n la mas baja fue {prom_alumno12[2]} ")
    print(prom_alumno12)
    prom_alumno=0
    prom_alumno12.clear()
    prom_alumno1.clear()






 
# =============================================================================
# actividad A
# =============================================================================
class punto:
    def __init__(self,x,y):
        self.coordenada_x=x
        self.coordenada_y=y
        
    def cuadrante(self,coordenada_x,coordenada_y):
        if coordenada_x >0:
           if coordenada_y>0:
               a="cuadrante 1"
           else: 
               a="cuadrante 4"
        else:
            if coordenada_y>0:
                a="cuadrante 2"
            else:
                a="cuadrante 3"
        return a
    
c=punto(0,0)
f=int(input("ingrese coordenada x"))
g=int(input("ingrese coordenada y"))
c.coordenada_x=f
c.coordenada_y=g
print(c.cuadrante(f,g))
# =============================================================================
# actividad B
# =============================================================================

class recta:
    def __init__(self,a,b):
        self.pendiente=a
        self.variable_independiente=b
    def ordenada_al_origen(self,b):
        return b

    def ceros(self,a,b):
        c=(-b)/a
        return c
    
p=recta(0, 0)
f=int(input("ingrese pendiente"))
g=int(input("ingrese variable independiente"))
p.pendiente=f
p.variable_independiente=g
print(p.ceros(f,g),p.ordenada_al_origen(g))
        
# =============================================================================
# actividad C
# =============================================================================
        

class complejo:
    def __init__(self,realx,imagx):
        self.real=realx
        self.imag=imagx
        
    def __str__(self):
        return str(self.real)+"+"+str(self.imag)+"i"
    
    def sumaComplejos(self,cx):
        rea=self.real+cx.real
        ima=self.imag+cx.imag
        c3=complejo(rea,ima)
        return c3
    def multiplicaionComplejos(self,cx):
        rea=self.real*cx.real
        ima=self.imag*cx.imag
        c3=complejo(rea,ima)
        return c3
                        
re=int(input("Ingrese la parte real"))
im=int(input("Ingrese la parte imaginaria"))
c1=complejo(re,im)
c2=complejo(5,6)

c4=c1.sumaComplejos(c2)
c5=c1.multiplicaionComplejos(c2)
print(c4,c5)

# =============================================================================
# actividad E
# =============================================================================

class racional:
    def __init__(self,numer,denom):
        self.numerador=numer
        self.denominador=denom
        
    def cuadrado(self):
        n=self.numer**2
        d=self.denom**2
        rac= n+"/"+d
        return rac
    
    def sumaracionales(self,cx):
        if self.denominador!=cx.denominador:
            
            d=self.denominador*cx.denominador
            n=self.numerador*cx.denominador
            c2=n+(cx.numerador*self.denominador)
            
            return str(c2)+"/"+str(d)
        else:
            return str(self.numerador+cx.numerador)+"/"+str(self.denominador)
        
    def restaracionales(self,cx):
        if self.denominador!=cx.denominador:
            
            d=self.denominador*cx.denominador
            n=self.numerador*cx.denominador
            n2=cx.numerador*self.denominador
            c2=n-n2
            
            return str(c2)+"/"+str(d)
        else:
            return str(self.numerador-cx.numerador)+"/"+str(self.denominador)
        
c=racional(2, 3)
c1=racional(2, 2)
a=c.sumaracionales(c1)
b=c.restaracionales(c1)
print(a,b)


# =============================================================================
# actividad F
# =============================================================================

class fecha:
    def __init__(self,dia,mes,año):
        self.dia=dia
        self.mes=mes
        self.año=año
        if dia>31:
            print("[dia] numero invalido")
        if mes==0 and mes>12:
            print("[mes]numero invalido")
        if mes==2 and dia>28:
            print("[dia] numero invalido")
        else:
            print("fecha valida")
            
    def __str__(self):
         return str(self.dia)+"/"+str(self.mes)+"/"+str(self.año)
             
    def tiempo (self,cx):
       
        a=self.dia-cx.dia
        i=self.mes-cx.mes 
        p=self.año-cx.año
        tie=fecha(a, i, p)
        return tie
         
a=fecha(27, 2, 2002)
b=fecha(2, 2, 2000)
print(a,"\n",b)
print("han pasado",a.tiempo(b))


# =============================================================================
# actividad G
# =============================================================================

class rectangulo:
    def __init__(self,largo,ancho,color):
        self.largo=largo
        self.ancho=ancho
        self.color=color
        
    def perimetro(self):
        p=(self.ancho*2)+(self.largo*2)
        return p
    
    def area(self):
        are=self.ancho*self.largo
        return are
a=rectangulo(2, 3, "rojo")
print(a.area(),a.perimetro()) 


# =============================================================================
# actividad H
# =============================================================================

class circulo:
    def __init__(self,radio):
        self.radio=radio
        
    def perimetro_circulo(self):   
        return (2*3.14*self.radio)
    def diametro(self):
        return self.radio*2
    def area_circulo(self):
        return (3.14*(self.radio**2))
    
# =============================================================================
# actividad I
# =============================================================================
    
class vehiculo:
    def __init__(self,marca,año,kilometros):
        self.marca=marca
        self.año=año
        self.kilometros=kilometros
        
    def service(self):
        return ("su proximo service sera a los ", (self.kilometros+10000)," kilometros")
    
    def patentes(self):
        
        antiguedad=2022-self.año
        if antiguedad==13:
            return ("usted ya no debe abonar patentes")
        else:
            return ("usted debe serguir abonando patentes hasta dentro de ", (antiguedad-13),"años")
        

# =============================================================================
# actividad 2
# =============================================================================
            
class recta:
    def __init__(self,a,b):
        """ a: pendiente b: ordenada al origen """
        
        self.pendiente=a
        self.variable_independiente=b
        
    def __str__(self):
        return "y="+str(self.pendiente)+"x+"+str(self.variable_independiente)
    
    def ordenada_al_origen(self):
        return self.variable_independiente
    
    def get_pendiente(self):
        return self.pendiente
    
    def set_a(self,n):
        self.pendiente=n
        
    def set_b(self,n):
        self.variable_independiente=n
        
    def ceros(self,a,b):
        c=(-b)/a
        return c
a=0

while a!=7:
    print("""1. Definir 2 Nuevas Rectas. \n
    2. Obtener Ordenadas al Origen \n
    3. Obtener Pendientes \n
    4. Determinar si se cortan entre si. \n
    5. Determinar si una es paralela a la otra. \n
    6. Determinar si una es perpendicular a la otra. \n
    7. Salir
        """)
    a=int(input("ingrese el numero de la opcion"))
    r1=recta(0, 0)
    r2=recta(0, 0)
    
    while a!=7:    
        if a==1:
            print("y= ax + b")
            p=int(input("ingrese el termino a de su recta 1: "))
            p1=int(input("ingrese el termino b de su recta 1: "))
            r1.set_a(p)
            r1.set_b(p1)
            p2=int(input("ingrese el termino a de su recta 2: "))
            p3=int(input("ingrese el termino b de su recta 2: "))
            r2.set_a(p2)
            r2.set_b(p3)
            print(r1.__str__(),r2.__str__())
        
        print("""1. Definir 2 Nuevas Rectas. \n
        2. Obtener Ordenadas al Origen \n
        3. Obtener Pendientes \n
        4. Determinar si se cortan entre si. \n
        5. Determinar si una es paralela a la otra. \n
        6. Determinar si una es perpendicular a la otra. \n
        7. Salir
            """)
        a=int(input("ingrese el numero de la opcion:"))
        if a==2:
            print("la ordenada al origen de la recta 1 es",r1.ordenada_al_origen())
            print("la ordenada al origen de la recta 2 es",r2.ordenada_al_origen())
        if a==3:
            print("la pendiente de la recta 1 es", r1.get_pendiente())
            print("la pendiente de la recta 2 es", r2.get_pendiente())
        if a==4:
            if p!=p2:
                print("se intersectan")
            else:
                print("no se intersectan")
        if a==5:
            if p==p2:
                print("son paralelas")
            else:
                print("no son paralelas")
        if a==6:
            if (p-(-p2))==0:
                print("son perpendiculares")
            else:
                print("no son perpendiculares")
                
# =============================================================================
# actividad 3
# =============================================================================
 
class racional:
    def __init__(self,numer,denom):
        self.numerador=numer
        self.denominador=denom
        
    def set_numerador(self,n):
        self.numerador=n
         
    def set_denominador(self,n):
        self.denominador=n
    def __str__(self):
        return str(self.numerador)+"/"+str(self.denominador)
    
    def cuadrado(self):
        n=self.numer**2
        d=self.denom**2
        rac= n+"/"+d
        return rac
    
    def sumaracionales(self,cx):
        if self.denominador!=cx.denominador:
            
            d=self.denominador*cx.denominador
            n=self.numerador*cx.denominador
            c2=n+(cx.numerador*self.denominador)
            
            return str(c2)+"/"+str(d)
        else:
            return str(self.numerador+cx.numerador)+"/"+str(self.denominador)
        
    def restaracionales(self,cx):
        if self.denominador!=cx.denominador:
            
            d=self.denominador*cx.denominador
            n=self.numerador*cx.denominador
            n2=cx.numerador*self.denominador
            c2=n-n2
            
            return str(c2)+"/"+str(d)
        else:
            return str(self.numerador-cx.numerador)+"/"+str(self.denominador)


a=0

while a!=6:
    print("""1. Ingresar 2 nuevas fracciones .
2. Calcular la suma de ambas
3. Calcular la resta de ambas
4. Determinar el minimo comun multiplo
5. Determinar el maximo comun divisor
6. Salir
        """)
    a=int(input("ingrese el numero de la opcion"))
    r1=racional(0, 0)
    r2=racional(0, 0)
    
    while a!=6:    
        if a==1:
            p=int(input("ingrese el numerador: "))
            p1=int(input("ingrese el denominador "))
            r1.set_numerador(p)
            r1.set_denominador(p1)
            p2=int(input("Ingrese el numerador: "))
            p3=int(input("Ingrese el denominador: "))
            r2.set_numerador(p2)
            r2.set_denominador(p3)
            print(r1.__str__(),r2.__str__())
        
        print("""1. Ingresar 2 nuevas fracciones .
              2. Calcular la suma de ambas
              3. Calcular la resta de ambas
              4. Determinar el minimo comun multiplo
              5. Determinar el maximo comun divisor
              6. Salir
            """)
        a=int(input("ingrese el numero de la opcion:"))
        if a==2:
            print("la suma es",r1.sumaracionales(r2))
           
        if a==3:
            print("la resta es", r1.restaracionales(r2))
        if a==4:
            print("el minimo comun multiplo", r1.restaracionales(r2))
            
            

# =============================================================================
# actividad 4
# =============================================================================


cant_autos=int(input("que cantidad de autos hay en su familia:"))
lista_autos=[]
contador_autos=[]
for i in range(cant_autos):
    auto=input(f"ingrese la marca de su auto {i+1}").lower()
    lista_autos.append(auto)

for i in range(cant_autos):
    contador=0
    for j in range(cant_autos):
        if lista_autos[i]==lista_autos[j]:
            contador+=1
    contador_autos.append(contador)
        
for i in range(cant_autos):
    print(f"de la marca {lista_autos[i]} hay {contador_autos[i]}")        
    
# =============================================================================
# actividad 5
# =============================================================================
     
class circulo:
    def __init__(self,radio):
        self.radio=radio
    def set_radio(self,radio):
        self.radio=radio
    def perimetro_circulo(self):   
        return (2*3.14*self.radio)
    def diametro(self):
        return self.radio*2
    def area_circulo(self):
        return (3.14*(self.radio**2))
    

arch=open("radios.txt","w")
arch.write("1 \n")
arch.write("2 \n")
arch.close()

archivo=open("radios.txt","r")
block1=archivo.readlines()
blockint=[]
archivo.close()

circulos=[]

for i in range(len(block1)):
    blockint.append(float(block1[i]))
    c=circulo(blockint[i])
    circulos.append(c)
    
  
print("la cantidad de circulos que hay es ",len(block1))
print("el radio promedio es ", sum(blockint)/len(block1))

# =============================================================================
# actividad 6
# =============================================================================
      
class fecha:
    def __init__(self,dia,mes,año):
        self.dia=dia
        self.mes=mes
        self.año=año
        
    def set_dia(self,dia):
        if dia>31 or (self.mes==2 and dia>28) :
            print(dia," numero invalido")
        else:
            self.dia=dia
            
            
    def set_mes(self,mes):
        if mes==0 and mes>12:
            print(f"{mes}numero invalido")
        else:
            self.mes=mes
            
    def set_año(self,año):
            self.año=año
            
    def __str__(self):
         return str(self.dia)+"/"+str(self.mes)+"/"+str(self.año)
             
    
    def edad (self,cx):
       
        p=self.año-cx.año
        if p<0:
           return p*(-1)
        else:
            return p

r1=fecha(0, 0, 0)
p=int(input("ingrese el dia de nacimiento: "))
p1=int(input("ingrese el mes en el que nacio: "))
p2=int(input("ingrese el año en el que nacio: "))
r1.set_dia(p)
r1.set_mes(p1)
r1.set_año(p2)
fecha_actual=fecha(9, 9, 2022)
print("su edad es ", r1.edad(fecha_actual))


# =============================================================================
# actividad 7
# =============================================================================
    
class fecha:
    def __init__(self,dia,mes,año):
        self.dia=dia
        self.mes=mes
        self.año=año
        
    def set_dia(self,dia):
        if dia>31 or (self.mes==2 and dia>28) :
            print(dia," numero invalido")
        else:
            self.dia=dia
            
            
    def set_mes(self,mes):
        if mes==0 and mes>12:
            print(f"{mes}numero invalido")
        else:
            self.mes=mes
            
    def set_año(self,año):
            self.año=año
            
    def __str__(self):
         return str(self.dia)+"/"+str(self.mes)+"/"+str(self.año)
             

    def tiempo (self,cx):
        a=self.dia-cx.dia
        i=self.mes-cx.mes 
        p=self.año-cx.año
        if a<0:
            a1=a*(-1)
        else:
            a1=a
        if i<0:
            i1=i*(-1)
        else:
            i1=i
        if p<0:
            p1=p*(-1)
        else:
            p1=p
        tie=fecha(a1, i1, p1)
        return tie
    
r1=fecha(0, 0, 0)
p=int(input("ingrese el dia de nacimiento: "))
p1=int(input("ingrese el mes en el que nacio: "))
p2=int(input("ingrese el año en el que nacio: "))
r1.set_dia(p)
r1.set_mes(p1)
r1.set_año(p2)
fecha_actual=fecha(9, 9, 2022)
print("su antiguedad es ", r1.tiempo(fecha_actual))



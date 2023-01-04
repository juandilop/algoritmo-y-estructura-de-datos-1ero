# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:53:33 2022

@author: juan
"""

# =============================================================================
# actividad 1
# =============================================================================

x=3*230+2*-3
" O(1)"


# =============================================================================
# actividad 2
# =============================================================================

x =5*3-21
y = 3 * 2
print(x + y)

" O(1)"



# =============================================================================
# actividad 3
# =============================================================================

def es_par (n):
    if (n % 2 == 0):
        return True
    else:
        return False
"O(1)"


# =============================================================================
# actividad 4
# =============================================================================

n = int(input("Ingrese un numero n:"))
for x in range(n):
    print(x)

"O(n)"


# =============================================================================
# actividad 5
# =============================================================================

"""
if x == 0:
    # O(1)
else if x < 0:
    # O(log(n))
else:
    # O(n**2)
"""

"O(n**2)"


# =============================================================================
# actividad 6
# =============================================================================
palabra="puto"
def imprimir_doble (palabra ):
    for letra in palabra:
        print(letra)
    for letra in palabra:
        print(letra)

imprimir_doble(palabra)
"O(n)"


# =============================================================================
# actividad 7
# =============================================================================

def indice_primera_ocurrencia (n, vector ):
    for i in range(len(vector )):
        if vector[i] == n:
            return i
        return -1


"O(n)"

# =============================================================================
# actividad 8
# =============================================================================
def ocurrencias (n, vector ):
    indices = []
    for i in range(len(vector )):
        if vector[i] == n:
            indices.append(i)
            return indices


"O(n)"



# =============================================================================
# actividad 9
# =============================================================================

def sumas(nros ):
    print("Estos son todos los numeros que hay:")
    for n in nros:
        print(n)
        print("Estas son las sumas de a pares:")
        for primero in nros:
            for segundo in nros:
                print(primero + segundo)
                
"O(n**2)"
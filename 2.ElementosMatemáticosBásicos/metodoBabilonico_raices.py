# -*- coding: utf-8 -*-
"""
Cáculo de la raíz de un número positivo, con el 
método Babilónico

Actividad: Ver con cuantas cifras se aproxima correctamente
Probar= Para raiz de 7 aprox 2 ; 2 aprox 1 y 1.4 ; 11 aprox 3 
y poner el parametro 50.49  (50 dígitos y 49 cifras decimales) 
para formato 

@author: Roberto Méndez

Created on Thu Apr 25 21:40:20 2024
Editado: Jun/09/24
"""
import numpy as np

raiz = float(input("Dame el valor del cual quieres la raíz: "))
aprox = float(input("Da una aproximación: "))


for x in range(5):
    aprox = .5*(aprox + raiz/aprox)
    
print("La raíz aproximada de {0} es {1}"
         .format(raiz, aprox)) 

print("La raíz de {0} es {1:50.49} ".format(raiz, np.sqrt(raiz)))








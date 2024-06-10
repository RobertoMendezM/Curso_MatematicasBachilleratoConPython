# -*- coding: utf-8 -*-
"""
Objetivo: Mostrar el error producido por la represesentación de
números de punto flotanteen un cálculo simple

Subobjetivo: Forma correcta e incorrecta de comparar números de punto flotante

Referencia: Adaptado de Liang, Introduction to Java Programming and Data Structures
            pág. 87

Created on 14 Feb 2023
editado: 10/jun/26
@author: Roberto Méndez Méndez
"""

EPSILONM = 10**(-14)
   
print("Hago la cuenta ")
print("\t x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1")

x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1

print("Comparo directamente x == 0.5")
print("Es x == 0.5: ", x == 0.5)    


print("Usando la forma numérica")

if abs(x - 0.5) < EPSILONM:
    print( str(x) + " es aproximadamente 0.5" )      
    
    

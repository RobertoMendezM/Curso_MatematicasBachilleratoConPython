# -*- coding: utf-8 -*-
"""
Objetivo: Mostrar que la asociatividad y conmutatividad no
          es directamente válidad en python
          
Created on 7 Fri Sep 24 2021
Editado: 10/Jun/24

@author: Roberto Méndez
"""

a = 1
b = 10**(-16)
c = -1

print("En álgebra nos han dicho que (a + b) + c =  a + (b + c) \n" )
print("Entonces 1 + (-1 + 10^(-16))  = (1 - 1) + 10^(-16)   ")
print("REalizando las operacione de manera ingenua en Python: ")
print( (a + b) + c, " = ",  a + (b + c))


a = 1/3
b = 1/7
c = 2/3

print("En álgebra nos han dicho que  a + b + c =  a + c + b) \n" )
print("Entonces 1/3 + 1/7 - 2/3  = 1/3 - 2/3 + 1/7   ")

e = a - b + c
d = a + c - b
print("Realizando la operaciones: \n" +
       "1/3 - 1/7 + 2/3 = " , e , "\n y \n" +
       "1/3 + 2/3 - 1/7 = ", d)




# -*- coding: utf-8 -*-
"""
Curso: Matehmaticas con Python

Tema: Máximo común divisor y Algoritmo de Euclides

Condiciones:  a > 0 y b > 0 enteros 

Created on 18 Jun 2024 
@author: Roberto Méndez Méndez
"""

while True:
  a = int(input("Dame el primer entero: "))
  b = int(input("Dame el segundo entero: "))
  if a > 0 and b > 0:
      break
  print("  Ambos números deben ser mayores a 0 ")

q = a//b
r = a - b*q
while r != 0 :
  a = b
  b = r
  q = a//b
  r = a - b*q
print("El máximo común divisor es: ", b)
# -*- coding: utf-8 -*-
"""
Fibonacci hacia adelante

Referencia: Classic Computer Science Problems with Python
            pag 11   fib5.py 

Created on Fri Jun 14 2024

editor: Roberto Méndez Méndez
"""

def fib(n):
    if n == 0:
        return n
    penultimo = 0
    ultimo = 1
    for _ in range(1, n):
        penultimo, ultimo = ultimo, penultimo + ultimo
    return ultimo

print(fib(100))

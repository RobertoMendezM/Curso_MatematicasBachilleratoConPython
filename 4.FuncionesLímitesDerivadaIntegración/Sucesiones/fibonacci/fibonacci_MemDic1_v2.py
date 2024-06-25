# -*- coding: utf-8 -*-
"""
Fibonacci con Memoria v2

Referencia: Classic Computer Science Problems with Python
            pag 10   fib3.py 

Created on Fri Jun 14 2024

editor: Roberto Méndez Méndez
"""

fibolist = {0: 0, 1: 1}

def fibMem(n):
    if n not in fibolist:
        fibolist[n] = fibMem(n-1) + fibMem(n-2)
    return fibolist[n]


print(fibMem(100))
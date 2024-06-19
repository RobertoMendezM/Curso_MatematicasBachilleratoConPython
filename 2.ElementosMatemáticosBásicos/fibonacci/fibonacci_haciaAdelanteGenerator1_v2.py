# -*- coding: utf-8 -*-
"""
Fibonacci con función Generator versión 2

Referencia: Classic Computer Science Problems with Python
            pag 12   fib9.py

Created on Fri Jun 14 2024

editor: Roberto Méndez Méndez
"""

def fibGenv2(n) :
    yield 0
    if n > 0:
        yield 1
    penultimo: int = 0
    ultimo:    int = 1
    for _ in range(1, n):
        penultimo, ultimo = ultimo, penultimo + ultimo
        yield ultimo

if __name__ == "__main__":
    for i in fibGenv2(100):
        print(i)



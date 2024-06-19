# -*- coding: utf-8 -*-
"""
Fibonacci con función Generator

Referencia: Classic Computer Science Problems with Python
            pag 12   fib9.py

Created on Fri Jun 14 2024

editor: Roberto Méndez Méndez
"""
from typing import Generator

def fibGen(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    penultimo: int = 0
    ultimo:    int = 1
    for _ in range(1, n):
        penultimo, ultimo = ultimo, penultimo + ultimo
        yield ultimo

if __name__ == "__main__":
    for i in fibGen(100):
        print(i)


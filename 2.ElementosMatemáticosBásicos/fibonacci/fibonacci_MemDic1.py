# -*- coding: utf-8 -*-
"""
Fibonacci con Memoria

Referencia: Classic Computer Science Problems with Python
            pag 10   fib3.py 

Created on Fri Jun 14 2024

editor: Roberto Méndez Méndez
"""

from typing import Dict


memo: Dict[int, int] = {0: 0, 1: 1}

def fibMem(n : int) -> int:
    if n not in memo:
        memo[n] = fibMem(n-1) + fibMem(n-2)
    return memo[n]


if __name__ == "__main__":
    print(fibMem(100))
    for z in memo:
        print(memo[z])

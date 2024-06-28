# -*- coding: utf-8 -*-
"""
Series de Taylor de ln(x) con sympy python

Tema: Series 

@author: Roberto Méndez

Fecha: Abril 24
"""
from sympy import symbols, ln

x = symbols('x')

lnx =  ln(x)

print(lnx.series(x, n=20, x0 = 1))

print(lnx.series(x, n=20, x0 = 1).removeO())


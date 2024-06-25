# -*- coding: utf-8 -*-
"""

Tema: Series con sympy python

@author: Roberto Méndez

Fecha: Abril 24
"""
from sympy import symbols, cos

x = symbols('x')

cosx =  cos(x)

print(cosx.series(x, n=20))

print(cosx.series(x, n=20).removeO())


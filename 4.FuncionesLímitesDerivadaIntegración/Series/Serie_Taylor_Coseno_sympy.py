# -*- coding: utf-8 -*-
"""
Series de Taylor de cos(x) con sympy python

Tema: Series 

@author: Roberto Méndez

Editado: 27 Jun 24
"""
from sympy import symbols, cos

x = symbols('x')

cosx =  cos(x)

print(cosx.series(x, n=20))

print(cosx.series(x, n=20).removeO())


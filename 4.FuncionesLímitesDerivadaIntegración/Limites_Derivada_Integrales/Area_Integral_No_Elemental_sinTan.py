# -*- coding: utf-8 -*-
"""
Objetivo: Obtener la Integral como área bajo la curva
          de una función que no tiene integral en términos de
          funciones elementales

Referencias: https://matplotlib.org/stable/api/_as_gen/matplotlib.
             pyplot.fill_between.html
             https://matplotlib.org/stable/gallery/lines_bars_and_markers/
             fill_between_demo.html#sphx-glr-gallery-lines-bars-and-markers-
             fill-between-demo-py
             https://rgbcolorpicker.com/0-1
         * sympy
             https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html


@author: Roberto Méndez Méndez

Editado 26 Jun 24
"""

import numpy as np
import matplotlib.pyplot as pl


paso = .00001
p = np.arange(-1,1,paso)


#  Versión cálculo directo

ft = np.sin(np.sqrt(3)*p)*np.tan(p)

pl.plot(p,ft, 'r')
pl.fill_between(p,ft,color=(1,.616,0,.459))
pl.title("sin[3^(1/2)t]tan[t]")
pl.show()

AreaFt = np.sum(paso*ft)

print("El área bajo la curva (numpy) es: ", AreaFt)


#  Versión con ciclos

import math

fx = []
area2 = 0
def fun1(x):
    return math.sin(math.sqrt(3)*x)*math.tan(x)
    

for h in p:
    y = fun1(h)
    fx.append(y)
    area2 += paso*y

print("El área bajo la curva con ciclos es: ", area2)    
    
fig, ax = pl.subplots()
ax.plot(p,fx)
ax.fill_between(p,ft,color=(1, 0.984, 0,.459))


#  Versión utilizando sympy


from sympy import Integral, symbols, sqrt, sin, tan
x = symbols('x')

integral = Integral(sin(sqrt(3)*x)*tan(x), (x, -1, 1))

print("El área bajo la curva con sympy : ", integral.evalf())



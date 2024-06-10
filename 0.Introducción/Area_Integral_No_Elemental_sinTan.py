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

Created on Mon Jun 10 13:45:06 2024

@author: Roberto Méndez Méndez
"""

import numpy as np
import matplotlib.pyplot as pl

paso = .01
p = np.arange(-1,1,paso)

ft = np.sin(np.sqrt(3)*p)*np.tan(p)

pl.plot(p,ft, 'r')
pl.fill_between(p,ft,color=(1,.616,0,.459))
pl.title("sin[3^(1/2)t]tan[t]")
#pl.show()

AreaFt = np.sum(paso*ft)

print("El área bajo la curva es: ", AreaFt)

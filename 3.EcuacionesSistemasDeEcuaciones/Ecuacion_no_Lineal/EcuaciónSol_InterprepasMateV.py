# -*- coding: utf-8 -*-
"""
Ejercicio ENP 2  Interprepas  Mate V

Referencias 
http://research.iac.es/sieinvens/python-course/matplotlib.html
https://claudiovz.github.io/scipy-lecture-notes-ES/intro/matplotlib/matplotlib.html

Created on Sun Jun 23 19:42:52 2024

15*3**(a-1)+3**(a + 1)+ 3**a = 27

15*3**(a-1)+3**(a + 1)+ 3**a - 27 = 0

f(x) = 15*3**(a-1)+3**(a + 1)+ 3**a - 27 

 f1(x) = 15*3**(a-1)+3**(a + 1)+ 3**a
 f2(x) = 27

@author: Roberto Méndez
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(.9,1.2, .001)
y = []

# Solución Forma 1

def fun1(a):
    return 15*3**(a-1)+3**(a + 1)+ 3**a

for a in x:
    y.append(fun1(a))

f2 = np.full(x.size, 27)

#Grafica forma 1
# Forma 1
plt.plot(x, y,'r', x,f2, 'y') 
    
# Solución Forma 2 
f1 = 15*3**(x-1)+3**(x + 1)+ 3**x
f2 = np.full(x.size, 27)


#Gráfica forma 2
fig, ax = plt.subplots()
ax.plot(x, f1, 'b', x, f2,'m') 
ax.grid('on')
ax.show()
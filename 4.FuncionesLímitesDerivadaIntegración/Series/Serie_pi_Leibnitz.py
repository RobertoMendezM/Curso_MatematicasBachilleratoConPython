# -*- coding: utf-8 -*-
"""
Pi  por fórmula de Leibnitz

     π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...

Tema: Series

Referencia: Classic Computer Science Problems with Python
            pag 19 

autor: Roberto Méndez Méndez

Editado: 27 Jun  2024
"""

import math
suma = 0
for n in range(1,200000):
     suma = suma + (-1)**(n + 1)*(1/(2*n - 1))
    
    
print(4*suma)
print(math.pi) 

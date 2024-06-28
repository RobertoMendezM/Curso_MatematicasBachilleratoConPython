# -*- coding: utf-8 -*-
"""
Calcular la suceción que converge a e

Tema: Suceción 

Subtema: ciclo for, formato print :>


@author: Roberto Méndez Méndez

Editado: Jun 27 2024


"""
import numpy as np

e = []
iteraciones = 100

for n in range(1, iteraciones + 1):   
    aprox = (1 + 1/n)**n
    e.append(aprox)
    print(f'{n:>7}, e aprox = {aprox:>18.15f}')


print("\n\nEl valor de e  calcudo en {0} \
iteraciones es = {1}".format(iteraciones, e[iteraciones-1]) )

print("\nEl valor de e con numpy es = ", np.e)


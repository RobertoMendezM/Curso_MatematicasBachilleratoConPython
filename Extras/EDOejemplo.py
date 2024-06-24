# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:37:49 2024

Editor: Roberto Menddez

https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.06-Python-ODE-Solvers.html

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


F = lambda t, s: np.cos(t) + np.sin(t)

t_eval = np.arange(0, np.pi, 0.1)
sol = solve_ivp(F, [0, np.pi], [0], t_eval=t_eval)

plt.figure(figsize = (12, 4))
plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('S(t)')
plt.show()
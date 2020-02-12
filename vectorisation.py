# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:18:50 2020

@author: Owner
"""

from numba import vectorize
@vectorize
def f_vec(x, y):
return np.cos(x**2 + y**2) / (1 + x**2 + y**2)
grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)
np.max(f_vec(x, y)) # Run once to compile
qe.tic()
np.max(f_vec(x, y))
qe.toc()
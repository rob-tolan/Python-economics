# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:24:34 2020

@author: Owner
"""

class Chaos:
"""
Models the dynamical system with :math:`x_{t+1} = r x_t (1 - x_t)`
"""
def __init__(self, x0, r):
"""
Initialize with state x0 and parameter r
"""
self.x, self.r = x0, r
def update(self):
"Apply the map to update state."
self.x = self.r * self.x *(1 - self.x)
def generate_sequence(self, n):
"Generate and return a sequence of length n."
path = []
for i in range(n):
path.append(self.x)
self.update()
return path
 ch = Chaos(0.1, 4.0) # x0 = 0.1 and r = 0.4
ch.generate_sequence(5) # First 5 iterates

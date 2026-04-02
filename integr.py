#Типы интегралов
"""
одномерный (quad)
двумерный (dbquad) - функция сначала принимает y потом x (обратный порядок)
тройной интеграл (tpquad) - сначала z потом y потом x
N-мерный интеграл (nquad)
"""

from scipy.integrate import quad, dblquad, tplquad, nquad
import numpy as np

#Одномерный интеграл
def f(x):
    return x**2
result, error = quad(f, 0, 2)
print(f"∫x2dx от 0 до 2 = {result}")
print(f"Погрешность {error}")

#Двумерный интеграл

def dbf(x, y):
    return x*y
result, error = dblquad(dbf, 0, 2, 0, 2)
print(f"∬x*y dxdy = {result}")

def tpf(x, y, z):
    return x*y*z

result, error = tplquad(tpf, 0, 2, 0, 3, 0, 2)
print(f"∭x*y*z dxdydz = {result}")

#Многомерный интеграл
def nf(x1, x2, x3, x4):
    return x1+x2+x3+x4

#находим предел для каждого x
range = [(0, 2), (0,2), (0, 2), (0,2)]
result, error = nquad(nf, range)
print(result)
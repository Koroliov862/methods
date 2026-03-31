import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator
import matplotlib.pyplot as plt
import random

#Парабола
x = np.array([0, 1, 2, 3, 4, 5])
y = x**2 - 3*x + np.random.normal(0, 0.5, 6)

# x_lin = np.linspace(0, 5)
# y_lin = np.interp(x_lin, x, y)

# plt.plot(x_lin , y_lin, 'b-', label = "линейная интерполяция")
# plt.plot(x, y, 'ro', label="Исходные точки")
# plt.legend()
# plt.grid(True)
# plt.show()

poly_lagrange = lagrange(x, y)
t = np.linspace(0, 5, 100)
plt.plot(t, poly_lagrange(t), 'b-', label = "Лагранж")
plt.plot(x, y, 'ro', label = "Исходные точки")
plt.legend()
plt.show()
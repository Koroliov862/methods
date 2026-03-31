import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator
import matplotlib.pyplot as plt
import random

#Синус
x= np.array([0, 1, 2, 3, 4, 5, 6])
y = np.sin(x)

poly_lagrange = lagrange(x, y)

t = np.linspace(0, 4, 100)

plt.plot(t, poly_lagrange(t), 'b-', label = "Лагранж")
plt.plot(x, y, 'go', markersize = 8)
plt.legend()
plt.show()
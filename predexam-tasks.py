import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator, CubicSpline
import matplotlib.pyplot as plt
#1
#=======================================================================================

x = np.array([15, 18, 22, 20])
y = np.array([8, 10, 13, 16])

newton_poly = KroghInterpolator(x, y)
time = np.array([12, 14, 15.5])
for i in time:
    print(f"Температура в {i}: {newton_poly(i)}")

plt.plot(time, newton_poly(time), 'b-', label = "Ньютон")
plt.plot(x, y, 'ro', label ="Исходные Точки")
plt.legend()
plt.grid(True)
plt.show()
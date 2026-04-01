#Рассчёт сплайнов
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, UnivariateSpline, PchipInterpolator
import random

# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([2, 8, 4, 5, 1, 0])
# t = np.linspace(0, 5, 100)

# cs  = CubicSpline(x, y)

# plt.plot(t, cs(t))
# plt.plot(x, y, 'ro')
# plt.show()
#простой кубический сплайн


#Сглаживающие сплайны UnivariateSpline
# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([2, 8, 4, 5, 1, 0])
# t = np.linspace(0, 5, 100)
# spline = UnivariateSpline(x, y, s = 0.5) #s = 0 проходит через точки
# plt.plot(t, spline(t))
# plt.plot(x, y, 'ro')
# plt.show()



#сплайн Эрмита
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2, 8, 4, 5, 1, 0, -9, 1, -4, 0])
t = np.linspace(0, 10, 500)
phip = PchipInterpolator(x, y)
plt.plot(t, phip(t))
plt.plot(x, y, 'ro')
plt.show()
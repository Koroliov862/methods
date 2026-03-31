# import numpy as np
# import matplotlib.pyplot as plt

# # интерполяция соединение точек прямыми
# # известные точки

# x = np.array([0, 1, 2, 3, 4])
# y = np.array([1, 2, 0, 2, 1])

# # линейная интерполяция (просто соденияем точки)
# x_lin = np.linspace(0, 4, 100)
# y_lin = np.interp(x_lin, x, y)

# plt.plot(x_lin , y_lin, 'b-', label = "линейная интерполяция")
# plt.plot(x, y, label = "Исходные точки")
# plt.legend()
# plt.grid(True)
# plt.show()


#Готовые методы ньютона и лагранжа интерполяция из библиотеки scipy
# скипи надстройка над numpy (научная библиотека для работы с тяж )
import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator

import matplotlib.pyplot as plt


x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

# метод лагранжа в 1 строчку
poly_lagrange = lagrange(x, y)
# метод ньютона в 1 строчку
poly_newton = KroghInterpolator(x, y)

# проверка
t = np.linspace(0, 4, 100)

# отрисовочка
plt.plot(t, poly_lagrange(t), 'b-', label = "Лагранж")
plt.plot(t, poly_newton(t), 'r--', label = "Ньютон")
plt.plot(x, y, 'go', markersize = 8)
plt.legend()
plt.show()

#Синус
x= np.array([0, 1, 2, 3, 4, 5, 6])
y = np.sin(x)

#Парабола 
x = np.array([0, 1, 2, 3, 4, 5])
y = x**2 - 3*x + np.random.normal(0, 0.5, 8)

#Экспонента
x = np.array([0, 1, 2, 3, 4])
y = np.exp(x/2)

#Ломанная
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([1, 5, 2, 9, 3, 8, 4])

#Затухание
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.exp(-x/3)*np.cos(x**2)

import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator
import matplotlib.pyplot as plt
import random
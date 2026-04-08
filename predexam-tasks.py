import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator, CubicSpline
#1
#=======================================================================================

x = np.array([8, 10, 13, 16])
y = np.array([15, 18, 22, 20])

newton_poly = KroghInterpolator(x, y)
time = np.array([12, 14, 15.5])
for i in time:
    print(f"Температура в {i}: {newton_poly(i):.2f}°C")

poly_cubic = CubicSpline(x, y)
print(f"{newton_poly(9)} = {poly_cubic(9)}\n {newton_poly(17)} = {poly_cubic(17)}")

#2
#=======================================================================================

def func(x): return 1 / (1 + 25*x**2)

x = np.linspace(-1, 1, 6)
y = func(x)
poly_lagrange = lagrange(x, y)

x_dense = np.linspace(-1, 1, 500)
f_true = func(x_dense)
f_interp = poly_lagrange(x_dense)

# Абсолютная погрешность
error = np.abs(f_true - f_interp)

# Поиск максимума погрешности
max_error_idx = np.argmax(error)
x_max_error = x_dense[max_error_idx]
max_error_value = error[max_error_idx]

print(f"Максимальная погрешность: {max_error_value:.6f}")
print(f"Достигается при x ≈ {x_max_error:.6f}")

#3
#=======================================================================================

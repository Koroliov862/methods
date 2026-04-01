import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline, UnivariateSpline, PchipInterpolator
from scipy.interpolate import KroghInterpolator

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2, 8, 4, 5, 1, 0, -9, 1, -4, 0])

t = np.linspace(0, 9, 500)

y_linear = np.interp(t, x, y)

poly_lagrange = lagrange(x, y)
y_lagrange = poly_lagrange(t)

newton_interpolator = KroghInterpolator(x, y)
y_newton = newton_interpolator(t)

cs = CubicSpline(x, y, bc_type='natural') 
y_cubic = cs(t)

hermite = PchipInterpolator(x, y)
y_hermite = hermite(t)

smoothing_spline = UnivariateSpline(x, y, s=0.5)
y_smoothing = smoothing_spline(t)

plt.figure(figsize=(14, 8))

plt.plot(t, y_linear, 'b-', label='Линейная интерполяция', linewidth=2, alpha=0.8)
plt.plot(t, y_lagrange, 'g-', label='Лагранж (полином)', linewidth=2, alpha=0.7)
plt.plot(t, y_newton, 'c-', label='Ньютон (разделенные разности)', linewidth=2, alpha=0.7)
plt.plot(t, y_cubic, 'm-', label='Кубический сплайн', linewidth=2)
plt.plot(t, y_hermite, 'orange', label='Сплайн Эрмита (PCHIP)', linewidth=2)
plt.plot(t, y_smoothing, 'purple', label='Сглаживающий сплайн (s=0.5)', linewidth=2, linestyle='--')

plt.plot(x, y, 'ro', label='Исходные точки', markersize=8, markeredgecolor='black')

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Сравнение различных методов интерполяции', fontsize=14)
plt.legend(fontsize=10, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
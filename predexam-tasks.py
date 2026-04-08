import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator, CubicSpline
#1
#=======================================================================================

x = np.array([15, 18, 22, 20])
y = np.array([8, 10, 13, 16])

newton_poly = KroghInterpolator(x, y)
time = np.array([12, 14, 15.5])
for i in time:
    print(f"Температура в {i}: {newton_poly(i):.2f}°C")

poly_cubic = CubicSpline(x, y)
print(f"{newton_poly(9)} = {poly_cubic(9)}\n {newton_poly(17)} = {poly_cubic(17)}")
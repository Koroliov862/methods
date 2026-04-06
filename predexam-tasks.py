import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator, quad, dblquad, tplquad, nquad

#1
#=======================================================================================

temps = np.array([15, 18, 22, 20])
times = np.array([8, 10, 13, 16])

newton_inrep = KroghInterpolator(times, temps)

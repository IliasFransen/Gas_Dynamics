import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve
from scipy.interpolate import griddata


xi = np.linspace(-1, 1, 10)
yi = np.linspace(0, 1, 10)
zi = griddata(([0,1,1], [0,0,1]), [3,2,3], (xi[None, :], yi[:, None]), method='cubic')
plt.contourf(xi, yi, zi)

xi = np.linspace(0, 1, 10)
yi = np.linspace(0, 1, 10)
zi = griddata(([-1,0,1], [1,0,1]), [3,2,3], (xi[None, :], yi[:, None]), method='cubic')
plt.contourf(xi, yi, zi)


plt.show()
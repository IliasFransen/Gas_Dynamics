import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve
from scipy.interpolate import griddata
import seaborn as sns

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle
from Task2_Regions import region_0, region_1, region_2, region_3
from Task2_Fans4_5 import coord_B, region4, point_BC, region5_sym, region5_gen
from Task2_Fans6_7 import coord_D, point_DF, region7_sym, region7_gen
from Task2_Fans8_9 import region9_gen, region9_sym, coord_H, pointHK
from Task2_Lines import Lines
from Calculator import Calculator

#define variables
M_0 = 2      #inlet mach number
P_a = 101325 #ambient pressure in Pa
g = 1.4      #specific heat ratio
phi_0 = 0    #angle in 0 (rad)
phi_2 = 0    #angle in 2 (rad)
phi_10 = 0   #angle in 10 (rad)
y_A = 1      #nozzle height (m)
x_A = 0      #nozzle end (m)

#number of lines in fans (including edges)
lines = False
n=6

def colors(Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9):

    #region 1
    #create x and y array for region 1
    #always take 10 points in y uniform regions
    m = 100
    y_range = np.linspace(x_A, y_A, m, endpoint = False)
    #create points between characteristic lines and inlet
    x_1 = np.array([])
    y_1 = np.array([])
    nu_1 = np.array([])
    M_1 = np.array([])
    phi_1 = np.array([])
    mu_1 = np.array([])

    #get slope of region 4's first char
    gamma_min_slope_4 = math.tan(val_4[0][2]-val_4[0][3])
    for i in range(m):
        x_temp = np.linspace(x_A, (y_range[i]-y_A)/math.tan(gamma_min_slope_4)+x_A, m-i, endpoint = True)
        y_temp = np.ones(m-i)*y_range[i]
        nu_temp = np.ones(m-i)*Val_1[0]
        M_temp = np.ones(m-i)*Val_1[1]
        phi_temp = np.ones(m-i)*Val_1[2]
        mu_temp = np.ones(m-i)*Val_1[3]

        x_1 = np.append(x_1, x_temp)
        y_1 = np.append(y_1, y_temp)
        nu_1 = np.append(nu_1, nu_temp)
        M_1 = np.append(M_1, M_temp)
        phi_1 = np.append(phi_1, phi_temp)
        mu_1 = np.append(mu_1, mu_temp)

        
    
    #create array with values of region 1
    Reg_1 = np.vstack((nu_1, M_1, phi_1, mu_1, x_1, y_1)).T


    # Contour plot
    plt.figure(figsize=(10, 5))
    xi = np.linspace(min(Reg_1.T[4]), max(Reg_1.T[4]), 100)
    yi = np.linspace(min(Reg_1.T[5]), max(Reg_1.T[5]), 100)
    zi = griddata((Reg_1.T[4], Reg_1.T[5]), Reg_1.T[1], (xi[None, :], yi[:, None]), method='cubic')

    plt.contourf(xi, yi, zi, levels=14, cmap='viridis')

    



        

    




def Main():
    Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9 = Calculator(M_0, phi_0, g, P_a, n, x_A, y_A)
    if lines:
        Lines(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A)

    colors(Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    Main()


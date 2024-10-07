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

def Reg_0_color(m, Val_0, val_5, x_A, y_A):
    xi = np.linspace(x_A, val_5[0][0][4], m)
    yi = np.linspace(0, y_A, m)
    zi = griddata(([x_A,0,val_5[0][0][4]], [y_A,0,val_5[0][0][5]]), [Val_0[1], Val_0[1], Val_0[1]], (xi[None, :], yi[:, None]), method='cubic')

    plt.contourf(xi, yi, zi)
    


def colors (Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9):

    m = 100
    
    Reg_0_color(m, Val_0, val_5, x_A, y_A)



        

def Main():
    Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9 = Calculator(M_0, phi_0, g, P_a, n, x_A, y_A)
    if lines:
        Lines(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A)

    colors(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    Main()


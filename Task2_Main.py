import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve
from scipy.interpolate import griddata
import seaborn as sns
import matplotlib.tri as tri

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle
from Task2_Regions import region_0, region_1, region_2, region_3
from Task2_Fans4_5 import coord_B, region4, region5_sym, region5_gen
from Task2_Fans6_7 import coord_D, region7_sym, region7_gen
from Task2_Fans8_9 import region9_gen, region9_sym, coord_H, pointHK
from Task2_Lines import Lines
from Calculator import Calculator
from Task2_Colors import Reg_0_color, Reg_1_color, Reg_2_color, Reg_3_color, Reg_4_colors, Reg_5_colors, Reg_6_colors, Reg_7_colors, Reg_8_colors, Reg_9_colors

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

plot = True
lines = True
n=7





def colors (Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, x_A, y_A, n):

    m = 100
    x = np.array([])
    y = np.array([])
    M = np.array([])
    x_0, y_0, M_0 = Reg_0_color(m, Val_0, val_5, x_A, y_A)
    x_1, y_1, M_1 = Reg_1_color(m, Val_1, val_5, val_7, x_A, y_A)
    x_2, y_2, M_2 = Reg_2_color(m, Val_2, val_5, val_7, val_9, x_A, y_A)
    x_3, y_3, M_3 = Reg_3_color(m, Val_3, val_7, val_9)
    x_4, y_4, M_4 = Reg_4_colors(x_A, y_A, val_4, val_5, n)
    x_5, y_5, M_5 = Reg_5_colors(val_5,n)
    x_6, y_6, M_6 = Reg_6_colors(val_5, val_7, n)
    x_7, y_7, M_7 = Reg_7_colors(val_7,n)
    x_8, y_8, M_8 = Reg_8_colors(val_7, val_9, n)
    x_9, y_9, M_9 = Reg_9_colors(val_9,n)


    x = np.concatenate((x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9))
    y = np.concatenate((y_0, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9))
    M = np.concatenate((M_0, M_1, M_2, M_3, M_4, M_5, M_6, M_7, M_8, M_9))

    triang = tri.Triangulation(x, y)

    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal')
    tcf = ax1.tricontourf(triang, M)
    fig1.colorbar(tcf)


    if lines:
        Lines(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A)

    if plot:
        plt.show()
        

def Main():
    Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9 = Calculator(M_0, phi_0, g, P_a, n, x_A, y_A)
    
    colors(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, x_A, y_A, n)
    

    
if __name__ == "__main__":
    Main()

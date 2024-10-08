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
lines = True
plot = True
n=5


def Reg_0_color(m, Val_0, val_5, x_A, y_A):
    xi = np.linspace(x_A, val_5[0][0][4], m)
    yi = np.linspace(0, y_A, m)
    zi = griddata(([x_A,0,val_5[0][0][4]], [y_A,0,val_5[0][0][5]]), [Val_0[1], Val_0[1], Val_0[1]], (xi[None, :], yi[:, None]), method='cubic')

    plt.contourf(xi, yi, zi)
    

def Reg_1_color(m, Val_1, val_5, val_7, x_A, y_A):
    xi = np.linspace(x_A, val_7[0][0][4], m)
    yi = np.linspace(val_5[0][-1][5], val_7[0][0][5], m)
    zi = griddata(([x_A,val_5[0][-1][4], val_7[0][0][4]], [y_A,val_5[0][-1][5], val_7[0][0][5]]), [Val_1[1], Val_1[1], Val_1[1]], (xi[None, :], yi[:, None]), method='cubic')

    plt.contourf(xi, yi, zi)

def Reg_2_color(m, Val_2, val_5, val_7, val_9, x_A, y_A):
    xi = np.linspace(val_5[-1][-1][4], val_9[0][0][4], m)
    yi = np.linspace(0, val_7[0][-1][5], m)
    zi = griddata(([val_5[-1][-1][4], val_7[0][-1][4], val_9[0][0][4]], [val_5[-1][-1][5], val_7[0][-1][5],val_9[0][0][5]]), [Val_2[1], Val_2[1], Val_2[1]], (xi[None, :], yi[:, None]), method='cubic')

    plt.contourf(xi, yi, zi)

def Reg_4_colors (x_A, y_A, val_4, val_5, n):
    
    #take 100 points along each line
    m = 100


    Val_4 = np.zeros((m*n,6))

    for i in range(n):
        x_4 = np.linspace(x_A, val_5[0][i][4], m+2)[1:-1]
        slope = math.tan(val_4[i][2]-val_4[i][3])
        for j in range(m):
            y_4 = slope*(x_4[j]-x_A) + y_A
            Val_4[i*m+j] = np.append(val_4[i], [x_4[j], y_4])

    #interpolate the values for plotting
    xi = np.linspace(min(Val_4[:,4]), max(Val_4[:,4]), 100)
    yi = np.linspace(min(Val_4[:,5]), max(Val_4[:,5]), 100)
    zi = griddata((Val_4[:,4], Val_4[:,5]), Val_4[:,1], (xi[None, :], yi[:, None]), method='cubic')
    
    plt.contourf(xi, yi, zi)


def Reg_5_colors (val_5,n):

    x_5 = np.array([])
    y_5 = np.array([])
    M_5 = np.array([])

    for i in range(n):
        
        for j in range(i,n):
            x_5 = np.append(x_5, val_5[i][j][4])
            y_5 = np.append(y_5, val_5[i][j][5])
            M_5 = np.append(M_5, val_5[i][j][1])

    xi = np.linspace(min(x_5), max(x_5), 100)
    yi = np.linspace(min(y_5), max(y_5), 100)
    zi = griddata((x_5, y_5), M_5, (xi[None, :], yi[:, None]), method='cubic')

    plt.contourf(xi, yi, zi)

def Reg_6_colors (val_5, val_7, n):
    
    #take 100 points along each line
    m = 100

    Val_6 = np.zeros((m*n,6))

    for i in range(n):
        x_6 = np.linspace(val_5[i][-1][4], val_7[0][i][4], m+2)[1:-1]
        slope = math.tan(val_5[i][-1][2]+val_5[i][-1][3])
        for j in range(m):
            y_6 = slope*(x_6[j]-val_5[i][-1][4]) + val_5[i][-1][5]
            Val_6[i*m+j] = np.append(val_5[i][-1][:4], [x_6[j], y_6])

    #interpolate the values for plotting
    xi = np.linspace(min(Val_6[:,4]), max(Val_6[:,4]), 100)
    yi = np.linspace(min(Val_6[:,5]), max(Val_6[:,5]), 100)
    zi = griddata((Val_6[:,4], Val_6[:,5]), Val_6[:,1], (xi[None, :], yi[:, None]), method='cubic')
    
    plt.contourf(xi, yi, zi)
        


def colors (Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, x_A, y_A, n):

    m = 100
    
    Reg_0_color(m, Val_0, val_5, x_A, y_A)
    Reg_1_color(m, Val_1, val_5, val_7, x_A, y_A)
    Reg_2_color(m, Val_2, val_5, val_7, val_9, x_A, y_A)
    Reg_4_colors(x_A, y_A, val_4, val_5, n)
    Reg_5_colors(val_5,n)
    Reg_6_colors(val_5, val_7, n)


    if lines:
        Lines(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    if plot:
        plt.show()
        

def Main():
    Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9 = Calculator(M_0, phi_0, g, P_a, n, x_A, y_A)
    
    colors(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, x_A, y_A, n)

    


if __name__ == "__main__":
    Main()


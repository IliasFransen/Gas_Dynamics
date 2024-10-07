import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle
from Task2_Regions import region_0, region_1, region_2, region_3
from Task2_Fans4_5 import coord_B, region4, point_BC, region5_sym, region5_gen
from Task2_Fans6_7 import coord_D, point_DF, region7_sym, region7_gen
from Task2_Fans8_9 import region9_gen, region9_sym, coord_H, pointHK
from Task2_Lines import Line_init
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
n=6

def Lines (Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A):



    #plot characteristics
    for i in range(n):

        x = np.array([])
        y = np.array([])

        #do region 4

        #figure out x-range, take 5 points between a and x_bc

        x_4 = np.linspace(x_A, val_5[0][i][4], 5, endpoint = False)

        #get corresponding y-values
        gamma_min_slope_4 = math.tan(val_4[i][2]-val_4[i][3])

        y_4 = gamma_min_slope_4*(x_4-x_A)+y_A

        #isolate x and y out of 5 array

        x_5 = np.array([])
        y_5 = np.array([])

        for j in range(i):
            x_5 = np.append(x_5, val_5[j][i][4])
            y_5 = np.append(y_5, val_5[j][i][5])


        for j in range(i,n):
            x_5 = np.append(x_5, val_5[i][j][4])
            y_5 = np.append(y_5, val_5[i][j][5])
                
        #region 6

        #get 5 x-points again
        x_6 = np.linspace(val_5[i][-1][4], val_7[0][i][4], 5+1, endpoint = False)[1:]

        #get slope of 6

        gamma_min_slope_6 = math.tan(val_5[i][-1][2]+val_5[i][-1][3])

        y_6 = gamma_min_slope_6*(x_6-val_5[i][-1][4])+val_5[i][-1][5]

        #region 7
        #isolate x and y out of 7 array

        x_7 = np.array([])
        y_7 = np.array([])

        for j in range(i):
            x_7 = np.append(x_7, val_7[j][i][4])
            y_7 = np.append(y_7, val_7[j][i][5])


        for j in range(i,n):
            x_7 = np.append(x_7, val_7[i][j][4])
            y_7 = np.append(y_7, val_7[i][j][5])

        #region 8

        #get 5 x-points again

        x_8 = np.linspace(val_7[i][-1][4], val_9[0][i][4], 5+1, endpoint = False)[1:]

        #get slope of 8

        gamma_min_slope_8 = math.tan(val_7[i][-1][2]-val_7[i][-1][3])
        

        y_8 = gamma_min_slope_8*(x_8-val_7[i][-1][4])+val_7[i][-1][5]

        #region 9

        #isolate x and y out of 9 array

        x_9 = np.array([])
        y_9 = np.array([])

        x_9 = np.array([])
        y_9 = np.array([])

        for j in range(i):
            x_9 = np.append(x_9, val_9[j][i][4])
            y_9 = np.append(y_9, val_9[j][i][5])


        for j in range(i,n):
            x_9 = np.append(x_9, val_9[i][j][4])
            y_9 = np.append(y_9, val_9[i][j][5])
        
        #create one long array for x and y

        x = np.concatenate((x_4, x_5, x_6, x_7, x_8, x_9))
        y = np.concatenate((y_4, y_5, y_6, y_7, y_8, y_9))

        plt.plot(x, y, color = 'black')

        

    




def Main():
    Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9 = Calculator(M_0, phi_0, g, P_a, n, x_A, y_A)
    Lines(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A)
    
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    Main()


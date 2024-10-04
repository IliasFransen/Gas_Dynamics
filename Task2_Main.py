import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle
from Task2_Regions import region_0, region_1, region_2, region_3, region_10
from Task2_Fans4_5 import coord_B, system4, region4, point_BC, region5_sym, region5_gen
from Task2_Fans6_7 import coord_D, point_DF
from Task2_Fans8_9 import region9_gen, region9_sym, coord_H, pointHK
from Task2_Lines import Line_init

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
n=4



def Main(M_0,phi_0,g,P_a,n):

    #CALCULATE ADDITIONAL PARAMETERS
    P_0 = 2*P_a
    P_t_0 = total_pressure(P_0, M_0,g)

    #CALCULATE UNIFORM REGIONS
    #val = nu, M, phi, mu, V_min, V_plus, Gamma_min_angle, Gamma_plus_angle
    Val_0 = region_0(M_0,phi_0,g,P_0)

    Val_1 = region_1(P_a,Val_0[5],P_t_0,g)

    Val_2 = region_2(Val_1[4],phi_2,g)

    Val_3 = region_3(Val_2[5],P_a,P_t_0,g)

    Val_10 = region_10(Val_3[4],phi_10,g)

    #CALCULATE DISCRETIZED LINES IN 4
    angles_4 = Line_init(Val_0[6],Val_1[6],n)

    #START DOING NON UNIFORM REGIONS

    #nu_p, M_p, phi_p, mu_p
    val_4 = np.array([Val_0[0],Val_0[1],Val_0[2],Val_0[3]])
    for i in range(n-2):
        val_4 = np.vstack(val_4, region4(Val_0[5], g, angles_4[i+1])[0:4])
    val_4 = np.vstack(val_4, np.array([Val_1[0],Val_1[1],Val_1[2],Val_1[3]]))

    #calculate location of B
    x_B, y_B = coord_B(y_A,M_0,phi_0,g,P_0, Val_0[6])

    #calculate points on BC with values
    xy_bc = np.array([point_BC(x_B, y_B, y_A, x_A, angles_4[0], Val_0[7])])
    for i in range(n-1):
        xy_bc = np.vstack(xy_bc, point_BC(x_B, y_B, y_A, x_A, angles_4[i+1], Val_0[7]))
    
    val_BC = np.hstack((val_4, xy_bc))


#one lines in 4, all values are the same

#calculate BC

#calculate region 5

#

if __name__ == "__main__":
    Main(M_0,phi_0,g,P_a,n) 
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from Task2_Functions import total_pressure
from Task2_Regions import region_0, region_1, region_2, region_3
from Task2_Fans4_5 import coord_B, region4, point_BC, region5_sym, region5_gen, point_BC_new
from Task2_Fans6_7 import coord_D, point_DF, region7_sym, region7_gen, point_DF_new
from Task2_Fans8_9 import region9_gen, region9_sym, coord_H, pointHK



def Calculator(M_0, phi_0, g, P_a, n, x_A, y_A):

    #CALCULATE ADDITIONAL PARAMETERS
    P_0 = 2*P_a
    P_t_0 = total_pressure(P_0, M_0,g)
    phi_2 = phi_0

    #CALCULATE UNIFORM REGIONS
    #val = nu, M, phi, mu, V_min, V_plus, Gamma_min_angle, Gamma_plus_angle
    Val_0 = region_0(M_0,phi_0,g,P_0)

    Val_1 = region_1(P_a,Val_0[5],P_t_0,g)

    Val_2 = region_2(phi_2, Val_1[4],g)

    Val_3 = region_3(Val_2[5],P_a,P_t_0,g)

    #START DOING NON UNIFORM REGIONS

    #calculate region 4
    d_phi = (Val_1[2]-Val_0[2]) / (n-1)

    #nu_p, M_p, phi_p, mu_p
    val_4 = np.array([Val_0[0],Val_0[1],Val_0[2],Val_0[3]])
    for i in range(n-2):
        val_4 = np.vstack((val_4, region4(Val_0[5], g, Val_0[2]+d_phi*(i+1))))

    val_4 = np.vstack((val_4, np.array([Val_1[0],Val_1[1],Val_1[2],Val_1[3]])))

    #calculate location of B
    x_B, y_B = coord_B(y_A, Val_0[6])

    val_BC = np.array(point_BC_new(x_B, y_B, Val_0[0], Val_0[1], Val_0[2], Val_0[3], y_A, x_A, val_4, n, 0, g))
    val_BC = np.vstack((val_BC,np.array(point_BC_new(x_B, y_B, Val_0[0], Val_0[1], Val_0[2], Val_0[3], y_A, x_A, val_4, n, 0, g))))
    for i in range(n-1):
        val_BC = np.vstack((val_BC, point_BC_new(val_BC[-1][4], val_BC[-1][5], val_BC[-1][0], val_BC[-1][1], val_BC[-1][2], val_BC[-1][3], y_A, x_A, val_4, n, i+1, g)))
    val_BC = val_BC[1:]

    #calculate points in 5
    val_5 = np.zeros((n,n,6))
    #first row is just BC
    for i in range(n):
        val_5[0][i] = val_BC[i]


    for j in range(1,n):

        for i in range(j,n):

            if i==j:
                #x_c, y_c, y_a, V_min_c, phi_a,g, mu_c, phi_c
                val_5[j][i] = (region5_sym(val_5[j-1][i][4], val_5[j-1][i][5], 0, val_5[j-1][i][0]+val_5[j-1][i][2], 0, g, val_5[j-1][i][3], val_5[j-1][i][2]))
            else:
                #x_a, y_a, x_d, y_d, V_plus_a, V_min_d, mu_a, g, phi_a, phi_d, mu_d
                val_5[j][i] = (region5_gen(val_5[j][i-1][4], val_5[j][i-1][5], val_5[j-1][i][4], val_5[j-1][i][5], val_5[j][i-1][0]-val_5[j][i-1][2], val_5[j-1][i][0]+val_5[j-1][i][2], val_5[j][i-1][3], g, val_5[j][i-1][2], val_5[j-1][i][2], val_5[j-1][i][3]))
            
    
    #calculate location of D
    #Gamma_plus_angle_1, x_C, y_C, y_A, x_A, phi_1
    x_D, y_D = coord_D(Val_1[7], val_5[0][-1][4], val_5[0][-1][5], y_A, x_A, Val_1[2])

#DO LIKE BC

    #get values in DF
    #take last column of 5, swap x and y with location from function
    val_DF = np.zeros((n,6))

    for i in range(n):
        #x_D, y_D, Gamma_min_angle_1, x_a, y_a, Gamma_plus_angle_a
        val_DF[i] = (np.hstack((val_5[i][-1][0:-2],point_DF(x_D, y_D, Val_1[6], val_5[i][-1][-2],val_5[i][-1][-1],val_5[i][-1][2]+val_5[i][-1][3])) ))

    val_DF = np.array(point_DF_new(x_D, y_D, Val_1[0], Val_1[1], Val_1[2], Val_1[3], val_5, n, 0, g))
    val_DF = np.vstack((val_DF,np.array(point_DF_new(x_D, y_D, Val_1[0], Val_1[1], Val_1[2], Val_1[3], val_5, n, 0, g))))
    for i in range(n-1):
        val_DF = np.vstack((val_DF, point_DF_new(val_DF[-1][4], val_DF[-1][5], val_DF[-1][0], val_DF[-1][1], val_DF[-1][2], val_DF[-1][3], val_5, n, i+1, g)))

    val_DF = val_DF[1:]



    #calculate region 7
    #similar to 5

    val_7 = np.zeros((n,n,6))
    #first row is just DF
    for i in range(n):
        val_7[0][i] = val_DF[i]

    for i in range(1,n):

        for j in range(1,i+1):

            if i==j:
                #x_c, y_c, mu_c, phi_c, V_plus_c, x_D, y_D, phi_D,P_a,g, P_t_0
                val_7[j][i] = np.array(region7_sym(val_7[j-1][i][4], val_7[j-1][i][5], val_7[j-1][i][3], val_7[j-1][i][2], val_7[j-1][i][0]-val_7[j-1][i][2], val_7[j-1][i-1][4], val_7[j-1][i-1][5], val_7[j-1][i-1][2], P_a, g, P_t_0))
            else:
                #x_a, y_a, x_d, y_d, V_min_a, V_plus_d, mu_a, g, phi_a, phi_d, mu_d
                val_7[j][i] = np.array(region7_gen(val_7[j][i-1][4], val_7[j][i-1][5], val_7[j-1][i][4], val_7[j-1][i][5], val_7[j][i-1][0]+val_7[j][i-1][2], val_7[j-1][i][0]-val_7[j-1][i][2], val_7[j][i-1][3], g, val_7[j][i-1][2], val_7[j-1][2][2], val_7[j-1][i][3]))


    #calculate location of H
    #Gamma_min_angle_2, x_F, y_F, y_H
    x_H, y_H = coord_H(Val_2[6], val_7[0][-1][4], val_7[0][-1][5], 0)

    #get values in HK
    #take last column of 7, swap x and y with location from function
    val_HK = np.zeros((n,6))
    
    val_HK [0] = np.hstack((val_7[0][-1][0:-2],x_H, y_H))

    for i in range(n-1):
        #x_H, y_H, mu_H, V_plus_H, phi_H, x_a, y_a, mu_a, phi_a, V_min_a, g
        val_HK [i+1] = np.hstack((val_7[i+1][-1][0:-2],pointHK(x_H, y_H, Val_2[3], Val_2[5], Val_2[2], val_7[i+1][-1][4], val_7[i+1][-1][5], val_7[i+1][-1][3], val_7[i+1][-1][2], val_7[i+1][-1][0]+val_7[i+1][-1][2], g) ))


    #calculate region 9
    #similar to 5

    val_9 = np.zeros((n,n,6))
    #first row is just HK
    for i in range(n):
        val_9[0][i] = val_HK[i]
    
    for j in range(1,n):

        for i in range(j,n):

            if i==j:
                #x_c, y_c, y_a, V_min_c, phi_a,g, mu_c, phi_c
                val_9[j][i] = np.array(region9_sym(val_9[j-1][i][4], val_9[j-1][i][5], 0, val_9[j-1][i][0] + val_9[j-1][i][2], 0, g, val_9[j-1][i][3], val_9[j-1][i][2]))
            else:
                #x_a, y_a, x_d, y_d, V_plus_a, V_min_d, mu_a, g, phi_a, phi_d, mu_d
                val_9[j][i] = np.array(region9_gen(val_9[j][i-1][4], val_9[j][i-1][5], val_9[j-1][i][4], val_9[j-1][i][5], val_9[j][i-1][0]-val_9[j][i-1][2], val_9[j-1][i][0] + val_9[j-1][i][2], val_9[j][i-1][3], g, val_9[j][i-1][2], val_9[j-1][i][2], val_9[j-1][i][3]))
     

    return Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve
from scipy.interpolate import griddata
import seaborn as sns

def Reg_0_color(m, Val_0, val_5, x_A, y_A):
    xi = np.linspace(x_A, val_5[0][0][4], m)
    yi = np.linspace(0, y_A, m)
    zi = griddata(([x_A,0,val_5[0][0][4]], [y_A,0,val_5[0][0][5]]), [Val_0[1], Val_0[1], Val_0[1]], (xi[None, :], yi[:, None]), method='cubic')

    #plt.contourf(xi, yi, zi)

    x_0 = [x_A,0,val_5[0][0][4]]
    y_0 = [y_A,0,val_5[0][0][5]]
    M_0 = [Val_0[1], Val_0[1], Val_0[1]]

    return x_0, y_0, M_0
    

def Reg_1_color(m, Val_1, val_5, val_7, x_A, y_A):
    xi = np.linspace(x_A, val_7[0][0][4], m)
    yi = np.linspace(val_5[0][-1][5], val_7[0][0][5], m)
    zi = griddata(([x_A,val_5[0][-1][4], val_7[0][0][4]], [y_A,val_5[0][-1][5], val_7[0][0][5]]), [Val_1[1], Val_1[1], Val_1[1]], (xi[None, :], yi[:, None]), method='cubic')

    #plt.contourf(xi, yi, zi)

    x_1 = [x_A,val_5[0][-1][4], val_7[0][0][4]]
    y_1 = [y_A,val_5[0][-1][5], val_7[0][0][5]]
    M_1 = [Val_1[1], Val_1[1], Val_1[1]]

    return x_1, y_1, M_1

def Reg_2_color(m, Val_2, val_5, val_7, val_9, x_A, y_A):
    xi = np.linspace(val_5[-1][-1][4], val_9[0][0][4], m)
    yi = np.linspace(0, val_7[0][-1][5], m)
    zi = griddata(([val_5[-1][-1][4], val_7[0][-1][4], val_9[0][0][4]], [val_5[-1][-1][5], val_7[0][-1][5],val_9[0][0][5]]), [Val_2[1], Val_2[1], Val_2[1]], (xi[None, :], yi[:, None]), method='cubic')

    #plt.contourf(xi, yi, zi)

    x_2 = [val_5[-1][-1][4], val_7[0][-1][4], val_9[0][0][4]]
    y_2 = [val_5[-1][-1][5], val_7[0][-1][5], val_9[0][0][5]]
    M_2 = [Val_2[1], Val_2[1], Val_2[1]]

    return x_2, y_2, M_2
        

def Reg_3_color(m, Val_3, val_7, val_9):
    x_7 = val_7[-1][-1][4]
    y_7 = val_7[-1][-1][5]
    x_9 = val_9[0][-1][4]
    y_9 = val_9[0][-1][5]
    slope_9 = val_9[0][-1][2]+val_9[0][-1][3]
    slope_3 = Val_3[2]
   
    #find the intersection point of two straigth lines
    x_max = (slope_3*x_7-y_7-slope_9*x_9+y_9)/(slope_3-slope_9)
    y_max = slope_3*(x_max-x_7)+y_7

    xi = np.linspace(val_7[-1][-1][4], x_max, m)
    yi = np.linspace(val_9[0][-1][5], val_7[-1][-1][5], m)
    zi = griddata(([val_7[-1][-1][4], val_9[0][-1][4], x_max], [val_7[-1][-1][5], val_9[0][-1][5], y_max]), [Val_3[1], Val_3[1], Val_3[1]], (xi[None, :], yi[:, None]), method='cubic')

    #plt.contourf(xi, yi, zi)

    x_3 = [val_7[-1][-1][4], val_9[0][-1][4], x_max]
    y_3 = [val_7[-1][-1][5], val_9[0][-1][5], y_max]
    M_3 = [Val_3[1], Val_3[1], Val_3[1]]

    return x_3, y_3, M_3

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
    
    #plt.contourf(xi, yi, zi)

    x_4 = Val_4[:,4]
    y_4 = Val_4[:,5]
    M_4 = Val_4[:,1]

    return x_4, y_4, M_4


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

    #plt.contourf(xi, yi, zi)

    return x_5, y_5, M_5

def Reg_6_colors (val_5, val_7, n):
    
    #take 100 points along each line
    m = 100

    Val_6 = np.zeros((m*n,6))

    for i in range(n):
        x_6 = np.linspace(val_5[i][-1][4], val_7[0][i][4], m+2)[1:-1]
        slope = math.tan((val_5[i][-1][2]+val_5[i][-1][3]+val_7[0][i][2]+val_7[0][i][3])/2)
        for j in range(m):
            y_6 = slope*(x_6[j]-val_5[i][-1][4]) + val_5[i][-1][5]
            Val_6[i*m+j] = np.append(val_5[i][-1][:4], [x_6[j], y_6])

    #interpolate the values for plotting
    xi = np.linspace(min(Val_6[:,4]), max(Val_6[:,4]), 100)
    yi = np.linspace(min(Val_6[:,5]), max(Val_6[:,5]), 100)
    zi = griddata((Val_6[:,4], Val_6[:,5]), Val_6[:,1], (xi[None, :], yi[:, None]), method='cubic')
    
    #plt.contourf(xi, yi, zi)

    x_6 = Val_6[:,4]
    y_6 = Val_6[:,5]
    M_6 = Val_6[:,1]

    return x_6, y_6, M_6

def Reg_7_colors (val_7,n):

    x_7 = np.array([])
    y_7 = np.array([])
    M_7 = np.array([])

    for i in range(n):
        
        for j in range(i,n):
            x_7 = np.append(x_7, val_7[i][j][4])
            y_7 = np.append(y_7, val_7[i][j][5])
            M_7 = np.append(M_7, val_7[i][j][1])
    
    xi = np.linspace(min(x_7), max(x_7), 100)
    yi = np.linspace(min(y_7), max(y_7), 100)
    zi = griddata((x_7, y_7), M_7, (xi[None, :], yi[:, None]), method='cubic')

    #plt.contourf(xi, yi, zi)

    return x_7, y_7, M_7


def Reg_8_colors (val_7, val_9, n):

    m = 100

    Val_8 = np.zeros((m*n,6))

    for i in range(n):
        x_8 = np.linspace(val_7[i][-1][4], val_9[0][i][4], m+2)[1:-1]
        slope = math.tan((val_7[i][-1][2]-val_7[i][-1][3] + val_9[0][i][2] - val_9[0][i][3])/2)
        for j in range(m):
            y_8 = slope*(x_8[j]-val_7[i][-1][4]) + val_7[i][-1][5]
            Val_8[i*m+j] = np.append(val_7[i][-1][:4], [x_8[j], y_8])    

    xi = np.linspace(min(Val_8[:,4]), max(Val_8[:,4]), 100)
    yi = np.linspace(min(Val_8[:,5]), max(Val_8[:,5]), 100)
    zi = griddata((Val_8[:,4], Val_8[:,5]), Val_8[:,1], (xi[None, :], yi[:, None]), method='cubic')

    #plt.contourf(xi, yi, zi)    

    x_8 = Val_8[:,4]
    y_8 = Val_8[:,5]
    M_8 = Val_8[:,1]

    return x_8, y_8, M_8

def Reg_9_colors (val_9,n):
    
        x_9 = np.array([])
        y_9 = np.array([])
        M_9 = np.array([])
    
        for i in range(n):
            
            for j in range(i,n):
                x_9 = np.append(x_9, val_9[i][j][4])
                y_9 = np.append(y_9, val_9[i][j][5])
                M_9 = np.append(M_9, val_9[i][j][1])
    
        xi = np.linspace(min(x_9), max(x_9), 100)
        yi = np.linspace(min(y_9), max(y_9), 100)
        zi = griddata((x_9, y_9), M_9, (xi[None, :], yi[:, None]), method='cubic')
    
        #plt.contourf(xi, yi, zi)

        return x_9, y_9, M_9


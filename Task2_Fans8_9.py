import math

from Task2_Functions import mach_number_nu, V_plus, V_min, Gamma_min_angle



#find location of H
#location on y=0
#follow Gamma-2 out of F
def coord_H(Gamma_min_angle_2, x_F, y_F, y_H):
    slope_2 = math.tan(Gamma_min_angle_2)
    x_H = x_F + (y_H-y_F)/slope_2
    return x_H, y_H


#solve in region 9
#exactly same as region 5

#find values along HK
#D is just the previous point, moves along with the characteristics
def pointHK(x_H, y_H, mu_H, V_plus_H, phi_H, x_a, y_a, mu_a, phi_a, V_min_a, g):
    # a is the value of the G- char on the line GF
    #calculate slope of gamma-GF
    Gamma_min_angle_a = Gamma_min_angle(phi_a,mu_a)
    slope_a = math.tan(Gamma_min_angle_a)

    #get slope from D
    slope_H = math.tan((phi_H+mu_H+phi_a+mu_a)/2)

    #get location of P
    x_p = (y_a-y_H+slope_H*x_H-x_a*slope_a)/(slope_H-slope_a)
    y_p = slope_a*(x_p-x_a)+y_a
    return x_p, y_p

def point_HK_new (x_B, y_B, nu_B, M_B, phi_B, mu_B, val_7, n, i, g):
    nu_p = (val_7[i][-1][0]+val_7[i][-1][2] + nu_B-phi_B)/2
    phi_p = (val_7[i][-1][0]+val_7[i][-1][2] - (nu_B - phi_B))/2
    M_p = mach_number_nu(nu_p,g)
    mu_p = math.asin(1/M_p)
    #get slopes of a and d
    slope_B = math.tan((mu_B+mu_p+phi_B+phi_p)/2)
    slope_7 = math.tan((-mu_p-val_7[i][-1][3]+phi_p+val_7[i][-1][2])/2)
    #get intersection point
    x_p = (slope_B*x_B-y_B-slope_7*val_7[i][-1][4]+val_7[i][-1][5])/(slope_B-slope_7)
    y_p = slope_B*(x_p-x_B)+y_B

    return  nu_p, M_p, phi_p, mu_p, x_p, y_p

    return  nu_p, M_p, phi_p, mu_p, x_p, y_p

#find points in region 9
#c is a point above a on the same char.
#literal copy of 5
def region9_sym (x_c, y_c, y_a, V_min_c, phi_a,g, mu_c, phi_c):
    nu_a = V_min_c - phi_a
    M_a = mach_number_nu(nu_a,g)
    mu_a = math.asin(1/M_a)
    slope_ca = math.tan((-mu_a-mu_c+phi_c+phi_a)/2)
    x_a = ((y_a-y_c)/slope_ca+x_c)
    return nu_a, M_a, 0, mu_a, x_a, y_a
    
#calculate a point in 9, NOT on the symmetry line
#d is above, a is below
def region9_gen (x_a, y_a, x_d, y_d, V_plus_a, V_min_d, mu_a, g, phi_a, phi_d, mu_d):
    nu_b = (V_min_d+V_plus_a)/2
    phi_b = (V_min_d-V_plus_a)/2
    M_b = mach_number_nu(nu_b,g)
    mu_b = math.asin(1/M_b)
    #get slopes of a and d
    slope_a = math.tan((mu_a+mu_b+phi_a+phi_b)/2)
    slope_d = math.tan((-mu_b-mu_d+phi_b+phi_d)/2)
    #get intersection point
    x_b = (slope_a*x_a-y_a-slope_d*x_d+y_d)/(slope_a-slope_d)
    y_b = slope_a*(x_b-x_a)+y_a
    return nu_b, M_b, phi_b, mu_b, x_b, y_b
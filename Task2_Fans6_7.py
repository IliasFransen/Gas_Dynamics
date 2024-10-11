import math

from Task2_Functions import mach_number_pres, prandtl_meyer_angle, mach_number_nu, V_plus, V_min

#find the coordinate of D
def coord_D (Gamma_plus_angle_1, x_C, y_C, y_A, x_A, phi_1):
    #intersection of G+ from C and (straight) boundary starting in A
    Gamma_plus_slope = math.tan(Gamma_plus_angle_1)
    boundary_slope = math.tan(phi_1)
    x_D = (y_A-y_C+Gamma_plus_slope*x_C-boundary_slope*x_A)/(Gamma_plus_slope-boundary_slope)
    y_D = boundary_slope*(x_D-x_A)+y_A
    return x_D, y_D


def point_DF_new (x_B, y_B, nu_B, M_B, phi_B, mu_B, val_5, n, i, g):
    nu_p = (val_5[i][-1][0]-val_5[i][-1][2] + nu_B+phi_B)/2
    phi_p = (-val_5[i][-1][0]+val_5[i][-1][2] + (nu_B + phi_B))/2
    M_p = mach_number_nu(nu_p,g)
    mu_p = math.asin(1/M_p)
    #get slopes of a and d
    slope_B = math.tan((-mu_B-mu_p+phi_B+phi_p)/2)
    slope_5 = math.tan((mu_p+val_5[i][-1][3]+phi_p+val_5[i][-1][2])/2)
    #get intersection point
    x_p = (slope_B*x_B-y_B-slope_5*val_5[i][-1][4]+val_5[i][-1][5])/(slope_B-slope_5)
    y_p = slope_B*(x_p-x_B)+y_B
    return  nu_p, M_p, phi_p, mu_p, x_p, y_p

#calculate a point in 7, on the symmetry line
#c is a point on DF
#D is the previous point on the edge, moves along
def region7_sym (x_c, y_c, mu_c, phi_c, V_plus_c, x_D, y_D, phi_D,P_a,g, P_t_0 ):
    M_a = mach_number_pres(P_t_0, P_a,g)
    nu_a = prandtl_meyer_angle(M_a,g)
    mu_a = math.asin(1/M_a)
    phi_a = nu_a - V_plus_c

    slope_ca = math.tan((mu_a+mu_c+phi_c+phi_a)/2)
    slope_Da = math.tan((phi_a+phi_D)/2)
    x_a = (y_c-y_D+slope_Da*x_D-x_c*slope_ca)/(slope_Da-slope_ca)
    y_a = slope_ca*(x_a-x_c)+y_c
    return nu_a, M_a, phi_a, mu_a, x_a, y_a

#calculate a point in 7, NOT on the symmetry line
#a is above, d is below
def region7_gen (x_a, y_a, x_d, y_d, V_min_a, V_plus_d, mu_a, g, phi_a, phi_d, mu_d):
    nu_b = (V_plus_d+V_min_a)/2
    phi_b = (V_min_a-V_plus_d)/2
    M_b = mach_number_nu(nu_b,g)
    mu_b = math.asin(1/M_b)
    #get slopes of a and d
    slope_a = math.tan((-mu_a-mu_b+phi_a+phi_b)/2)
    slope_d = math.tan((mu_b+mu_d+phi_b+phi_d)/2)
    #get intersection point
    x_b = (slope_a*x_a-y_a-slope_d*x_d+y_d)/(slope_a-slope_d)
    y_b = slope_a*(x_b-x_a)+y_a
    return nu_b, M_b, phi_b, mu_b, x_b, y_b
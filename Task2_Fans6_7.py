import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle
from Task2_Regions import region_0, region_1, region_2, region_3
from Task2_Fans4_5 import coord_B, system4, region4, point_BC, region5_sym, region5_gen



#find the coordinate of D
def coord_D (Gamma_plus_angle_1, x_C, y_C, y_A, x_A, phi_1):
    #intersection of G+ from C and (straight) boundary starting in A
    Gamma_plus_slope = math.tan(Gamma_plus_angle_1)
    boundary_slope = math.tan(phi_1)
    x_D = (y_A-y_C+Gamma_plus_slope*x_C-boundary_slope*x_A)/(Gamma_plus_slope-boundary_slope)
    y_D = boundary_slope*(x_D-x_A)+y_A
    return x_D, y_D

#find values along DF
#D is just the previous point, moves along with the characteristics
def point_DF (x_D, y_D, Gamma_min_angle_1, x_a, y_a, Gamma_plus_angle_a):
    #use the point a, where characteristics meet line CE
    slope_a = math.tan(Gamma_plus_angle_a)
    slope_D = math.tan(Gamma_min_angle_1)
    #calculate x and y in p, where both slopes meet (approx)
    x_p = (y_a-y_D+slope_D*x_D-x_a*slope_a)/(slope_D-slope_a)
    y_p = slope_a*(x_p-x_a)+y_a
    return x_p, y_p

#calculate a point in 7, on the symmetry line
#c is a point on DF
#D is the previous point on the edge, moves along
def region7_sym (x_c, y_c, mu_c, phi_c, V_plus_c, x_D, y_D, phi_D,P_a,g, P_t_0 ):
    M_a = mach_number_pres(P_t_0, P_a,g)
    nu_a = prandtl_meyer_angle(M_a,g)
    mu_a = math.asin(1/M_a)
    phi_a = nu_a - V_plus_c
    V_min_a = nu_a + phi_a

    slope_ca = math.tan((mu_a+mu_c+phi_c+phi_a)/2)
    slope_Da = math.tan((phi_a+phi_D)/2)
    x_a = (y_c-y_D+slope_Da*x_D-x_c*slope_ca)/(slope_Da-slope_ca)
    y_a = slope_ca*(x_a-x_c)+y_c
    return x_a, y_a, mu_a, nu_a, M_a, V_min_a, phi_a

#calculate a point in 7, NOT on the symmetry line
#a is above, d is below
def region7_gen (x_a, y_a, x_d, y_d, V_min_a, V_plus_d, mu_a, g, phi_a, phi_d, mu_d):
    nu_b = (V_plus_d+V_min_a)/2
    phi_b = (V_min_a-V_plus_d)/2
    M_b = mach_number_nu(nu_b,g)
    mu_b = math.asin(1/M_b)
    V_plus_b = V_plus(phi_b,nu_b)
    V_min_b = V_min(phi_b,nu_b)
    #get slopes of a and d
    slope_d = math.tan((mu_a+mu_b+phi_a+phi_b)/2)
    slope_a = math.tan((-mu_b-mu_d+phi_b+phi_d)/2)
    #get intersection point
    x_b = (slope_a*x_a-y_a-slope_d*x_d+y_d)/(slope_a-slope_d)
    y_b = slope_a*(x_b-x_a)+y_a
    return x_b, y_b, mu_b, nu_b, M_b, phi_b, V_plus_b, V_min_b
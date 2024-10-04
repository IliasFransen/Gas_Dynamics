import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle
from Task2_Regions import region_0, region_1, region_2, region_3


#define system to be solved for region 4
def system4 (nu_p, mu_p, M_p, phi_p, V_plus_0, g, delta):
    #make a system for fsolve to solve
    eq = (V_plus_0 - (nu_p - phi_p),
          phi_p - nu_p - delta, 
          mu_p - math.asin(1/M_p), 
          mach_number_nu(nu_p,g) - M_p)
    return eq

    
#calculate any point in 4
def region4 (V_plus_0, g, delta):
    #initial guess
    mu_p_ini = 0.1
    nu_p_ini = 0.1
    M_p_ini = 1.5
    phi_p_ini = 0.1
    #solve system
    mu_p, nu_p, M_p, phi_p = fsolve(system4, (nu_p_ini, mu_p_ini, M_p_ini, phi_p_ini), args=(V_plus_0, g, delta))
    return nu_p, M_p, phi_p, mu_p

print(region4(0,1.4,0.1))

#calcuate Coordinate of B
def coord_B(y_A,M_0,phi_0,g,P_0, Gamma_min_angle_0):
    #calculate location of B
    x_B = (0-y_A)/math.tan(Gamma_min_angle_0)
    y_B = 0
    return x_B, y_B

#calculates locaitons on BC
def point_BC (x_B, y_B, y_A, x_A, delta_p, Gamma_plus_angle_0):
    x_P = (y_B - y_A + math.tan(delta_p)*x_A-math.tan(Gamma_plus_angle_0)*x_A)/(-math.tan(Gamma_plus_angle_0)+math.tan(delta_p))
    y_P = math.tan(Gamma_plus_angle_0)*(x_P-x_A)+y_A
    return x_P, y_P

#calculate a point in 5, on the symmetry line
#c is a point above a on the char.
def region5_sym (x_c, y_c, y_a, V_min_c, phi_a,g, mu_c, phi_c):
    nu_a = V_min_c - phi_a
    M_a = mach_number_nu(nu_a,g)
    mu_a = math.asin(1/M_a)
    slope_ca = math.tan((-mu_a-mu_c+phi_c+phi_a)/2)
    x_a = ((y_a-y_c)/slope_ca+x_c)
    V_plus_a = V_plus(phi_a,nu_a)
    return x_a, y_a, mu_a, nu_a, M_a, V_plus_a

#calculate a point in 5, NOT on the symmetry line
#d is above, a is below
def region5_gen (x_a, y_a, x_d, y_d, V_plus_a, V_min_d, mu_a, g, phi_a, phi_d, mu_d):
    nu_b = (V_min_d+V_plus_a)/2
    phi_b = (V_min_d-V_plus_a)/2
    M_b = mach_number_nu(nu_b,g)
    mu_b = math.asin(1/M_b)
    V_plus_b = V_plus(phi_b,nu_b)
    V_min_b = V_min(phi_b,nu_b)
    #get slopes of a and d
    slope_a = math.tan((mu_a+mu_b+phi_a+phi_b)/2)
    slope_d = math.tan((-mu_b-mu_d+phi_b+phi_d)/2)
    #get intersection point
    x_b = (slope_a*x_a-y_a-slope_d*x_d+y_d)/(slope_a-slope_d)
    y_b = slope_a*(x_b-x_a)+y_a
    return x_b, y_b, mu_b, nu_b, M_b, phi_b, V_plus_b, V_min_b

#calculate point C
#the coordinate of C can be found by picking a point the rightmost characteristic of fan 4 (has the same values as region 1)

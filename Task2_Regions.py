import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from Task2_Functions import total_pressure, mach_number_pres, mach_angle, prandtl_meyer_angle, func, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle

#################################################CALCULATE UNIFORM REGIONS#################################################

#calculate region 0
def region_0(M_0,phi_0,g,P_0):
    nu_0 = prandtl_meyer_angle(M_0,g)
    V_plus_0 = V_plus(phi_0,nu_0)
    V_min_0 = V_min(phi_0,nu_0)
    mu_0 = mach_angle(M_0)
    Gamma_min_angle_0 = Gamma_min_angle(phi_0,mu_0)
    Gamma_plus_angle_0 = Gamma_plus_angle(phi_0,mu_0)
    return nu_0, M_0, phi_0, mu_0, V_min_0, V_plus_0, Gamma_min_angle_0, Gamma_plus_angle_0

#print(region_0(2,0,1.4,2*101325)) CHECK

#calculate region 1
def region_1(P_a,V_plus_0,P_t_0,g):
    M_1 = mach_number_pres(P_t_0, P_a,g)
    nu_1 = prandtl_meyer_angle(M_1,g)
    phi_1 = nu_1 - V_plus_0
    V_min_1 = V_min(phi_1,nu_1)
    V_plus_1 = V_plus(phi_1,nu_1)
    Gamma_min_angle_1 = Gamma_min_angle(phi_1,mach_angle(M_1))
    Gamma_plus_angle_1 = Gamma_plus_angle(phi_1,mach_angle(M_1))
    mu_1 = mach_angle(M_1)
    return nu_1, M_1, phi_1, mu_1, V_min_1, V_plus_1, Gamma_min_angle_1, Gamma_plus_angle_1

#print(region_1(101325,0.460,1585624,1.4)) CHECK

#calculate region 2
def region_2(phi_2,V_min_1,g):
    nu_2 = V_min_1 + phi_2
    M_2 = mach_number_nu(nu_2,g)
    V_plus_2 = V_plus(phi_2,nu_2)
    V_min_2 = V_min(phi_2,nu_2)
    Gamma_plus_angle_2 = Gamma_plus_angle(phi_2,mach_angle(M_2))
    Gamma_min_angle_2 = Gamma_min_angle(phi_2,mach_angle(M_2))
    mu_2 = mach_angle(M_2)
    return nu_2, float(M_2), phi_2, mu_2, V_min_2, V_plus_2, Gamma_min_angle_2, Gamma_plus_angle_2

#print(region_2(0,0.8592,1.4)) CHECK

#calculate region 3
def region_3(V_plus_2,P_a,P_t_0,g):
    M_3 = mach_number_pres(P_t_0, P_a,g)
    nu_3 = prandtl_meyer_angle(M_3,g)
    phi_3 = nu_3 - V_plus_2
    Gamma_min_angle_3 = Gamma_min_angle(phi_3,mach_angle(M_3))
    Gamma_plus_angle_3 = Gamma_plus_angle(phi_3,mach_angle(M_3))
    mu_3 = mach_angle(M_3)
    V_plus_3 = V_plus(phi_3,nu_3)
    V_min_3 = V_min(phi_3,nu_3)
    return nu_3, M_3, phi_3, mu_3, V_min_3, V_plus_3, Gamma_min_angle_3, Gamma_plus_angle_3

#print(region_3(0.8592,101325,1585624,1.4)) CHECK

#calculate region 10
def region_10 (phi_10, V_min_3,g):
    nu_10 = V_min_3 + phi_10
    M_10 = mach_number_nu(nu_10,g)
    V_plus_10 = V_plus(phi_10,nu_10)
    V_min_10 = V_min(phi_10,nu_10)
    Gamma_plus_angle_10 = Gamma_plus_angle(phi_10,mach_angle(M_10))
    Gamma_min_angle_10 = Gamma_min_angle(phi_10,mach_angle(M_10))
    mu_10 = mach_angle(M_10)
    phi_10
    return nu_10, M_10, phi_10, mu_10, V_min_10, V_plus_10, Gamma_plus_angle_10, Gamma_min_angle_10

#print(region_10(0,0.0.5,1.4)) CHECK
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

#################################################DEFINE FUNCTIONS#################################################

#calculates total pressure
def total_pressure(P, M,g):
    P_t = P*(1 + (g-1)/2*M**2)**(g/(g-1))
    return P_t

#print(total_pressure(10000,2,1.4)) CHECK

#calculates mach number from pressure
def mach_number_pres(P_t, P,g):
    M = math.sqrt((2/(g-1))*((P_t/P)**((g-1)/g)-1))
    return M

#print(mach_number_pres(total_pressure(1000,2,1.4),1000,1.4)) CHECK

#calculates the mach angle
def mach_angle(M):
    mu = math.asin(1/M)
    return mu

#print(mach_angle(2)) CHECK

#calculates prandtl-meyer angle
def prandtl_meyer_angle(M,g):
    nu = math.sqrt((g+1)/(g-1))*math.atan(math.sqrt((g-1)/(g+1)*(M**2-1)))-math.atan(math.sqrt(M**2-1))
    return nu

#print(prandtl_meyer_angle(2,1.4)) CHECK

#define function for fsolve
def func(M,nu,g):
    return math.sqrt((g+1)/(g-1))*math.atan(math.sqrt((g-1)/(g+1)*(M**2-1)))-math.atan(math.sqrt(M**2-1)) - nu

#calculates mach number from prandtl-meyer angle
def mach_number_nu(nu,g):
    #numerically solve for M
    M = fsolve(func, 1.5, args=(nu,g))
    return M

#print(mach_number_nu(prandtl_meyer_angle(2,1.4),1.4)) CHECK

#calculates V+
def V_plus(phi,nu):
    V_plus = nu - phi
    return V_plus

#print(V_plus(5,3)) CHECK

#calculates V-
def V_min(phi,nu):
    V_min = nu + phi
    return V_min

#print(V_min(5,3)) CHECK

#calculates Gamma+ slope
def Gamma_plus_angle(phi,mu):
    Gamma_plus_angle = mu + phi
    return Gamma_plus_angle

#CHECK

#calcutates Gamma- slope
def Gamma_min_angle(phi,mu):
    Gamma_min_angle = phi - mu
    return Gamma_min_angle

#print(Gamma_min_angle(5.0,4.9)) CHECK
import numpy as np
import math
from scipy.optimize import fsolve

#################################################DEFINE FUNCTIONS#################################################

#calculates total pressure
def total_pressure(P, M,g):
    P_t = P*(1 + (g-1)/2*M**2)**(g/(g-1))
    return P_t

#calculates mach number from pressure
def mach_number_pres(P_t, P,g):
    M = ((2/(g-1))*((P_t/P)**((g-1)/g)-1))**0.5
    return M

#calculates the mach angle
def mach_angle(M):
    mu = math.asin(1/M)
    return float(mu)

#calculates prandtl-meyer angle
def prandtl_meyer_angle(M,g):
    nu = ((g+1)/(g-1))**0.5 * math.atan(math.sqrt((g-1)/(g+1)*(M**2-1)))-math.atan(np.sqrt(M**2-1))
    return float(nu)

#define function for fsolve
def func(M,nu,g):
    return np.sqrt((g+1)/(g-1))*math.atan(np.sqrt((g-1)/(g+1)*(M**2-1)))-math.atan(np.sqrt(M**2-1)) - nu

#calculates mach number from prandtl-meyer angle
def mach_number_nu(nu,g):
    #numerically solve for M
    M = fsolve(func, 1.5, args=(nu,1.4))
    return float(M)

#calculates V+
def V_plus(phi,nu):
    V_plus = nu - phi
    return V_plus

#calculates V-
def V_min(phi,nu):
    V_min = nu + phi
    return V_min

#calculates Gamma+ slope
def Gamma_plus_angle(phi,mu):
    Gamma_plus_angle = mu + phi
    return Gamma_plus_angle

#calcutates Gamma- slope
def Gamma_min_angle(phi,mu):
    Gamma_min_angle = phi - mu
    return Gamma_min_angle

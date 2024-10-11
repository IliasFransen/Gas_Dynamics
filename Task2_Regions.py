from Task2_Functions import mach_number_pres, mach_angle, prandtl_meyer_angle, mach_number_nu, V_plus, V_min, Gamma_plus_angle, Gamma_min_angle

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


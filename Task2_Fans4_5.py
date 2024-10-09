import math

from Task2_Functions import mach_number_nu


    
#calculate any point in 4
def region4 ( V_plus_0, g, phi_p):
    nu_p = V_plus_0 + phi_p
    M_p = mach_number_nu(nu_p,g)
    mu_p = math.asin(1/M_p)
    return nu_p, M_p, phi_p, mu_p


#calcuate Coordinate of B
def coord_B(y_A, Gamma_min_angle_0):
    #calculate location of B
    x_B = (0-y_A)/math.tan(Gamma_min_angle_0)
    y_B = 0
    return x_B, y_B

#print(coord_B(1,2,0,1.4,101325,-0.5)) CHECK

#calculate a point on BC
#B is just the previous point, moves along with the characteristics

def point_BC_new (x_B, y_B, nu_B, M_B, phi_B, mu_B, y_A, x_A, val_4, n, i, g):
    nu_p = (val_4[i][0]+val_4[i][2] + nu_B-phi_B)/2
    phi_p = (val_4[i][0]+val_4[i][2] - (nu_B - phi_B))/2
    M_p = mach_number_nu(nu_p,g)
    mu_p = math.asin(1/M_p)
    #get slopes of a and d
    slope_B = math.tan((mu_B+mu_p+phi_B+phi_p)/2)
    slope_4 = math.tan((-mu_p-val_4[i][3]+phi_p+val_4[i][2])/2)
    #get intersection point
    x_p = (slope_B*x_B-y_B-slope_4*x_A+y_A)/(slope_B-slope_4)
    y_p = slope_B*(x_p-x_B)+y_B
    return  nu_p, M_p, phi_p, mu_p, x_p, y_p
    

#calculate a point in 5, on the symmetry line
#c is a point above a on the char.
def region5_sym (x_c, y_c, y_a, V_min_c, phi_a,g, mu_c, phi_c):
    nu_a = V_min_c - phi_a
    M_a = mach_number_nu(nu_a,g)
    mu_a = math.asin(1/M_a)
    slope_ca = math.tan((-mu_a-mu_c+phi_c+phi_a)/2)
    x_a = ((y_a-y_c)/slope_ca+x_c)
    return nu_a, M_a, 0, mu_a, x_a, y_a

#calculate a point in 5, NOT on the symmetry line
#d is above, a is below
def region5_gen (x_a, y_a, x_d, y_d, V_plus_a, V_min_d, mu_a, g, phi_a, phi_d, mu_d):
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
    return  nu_b, M_b, phi_b, mu_b, x_b, y_b


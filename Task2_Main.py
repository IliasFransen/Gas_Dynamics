import matplotlib.pyplot as plt

from Task2_Lines import Lines
from Calculator import Calculator
from Task2_Colors import colors

#define variables
M_0 = 2      #inlet mach number
P_a = 101325 #ambient pressure in Pa
g = 1.4      #specific heat ratio
phi_0 = 0    #angle in 0 (rad)
phi_2 = 0    #angle in 2 (rad)
phi_10 = 0   #angle in 10 (rad)
y_A = 1      #nozzle height (m)
x_A = 0      #nozzle end (m)

#number of lines in fans (including edges)
n=105
plot = True
lines = False
region_9 = False
pressure = False

###########################################################################################################################################   

def Main():
    Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, p_t_0 = Calculator(M_0, phi_0, g, P_a, n, x_A, y_A)
    
    colors(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, x_A, y_A, p_t_0, n, region_9, pressure)

    if lines:
        Lines(Val_0, Val_1, Val_2, Val_3, val_4, val_5, val_7, val_9, n, x_A, y_A, region_9)

    plt.xlabel("x-coordinate [m]")
    plt.ylabel("y-coordinate [m]")
    

    if plot:
        plt.show()
    
if __name__ == "__main__":
    Main()

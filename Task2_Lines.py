import numpy as np
import matplotlib.pyplot as plt
import math

#set up lines by angle from point A
#n is total line, including edges
def Line_init (Gamma_min_angle_0, Gamma_min_angle_1, n):
    #make an array of m angles between G-0 and G-1
    angles = np.linspace(Gamma_min_angle_0, Gamma_min_angle_1, n)
    return angles

#print(Line_init(0.5,0.3,5))    #CHECK

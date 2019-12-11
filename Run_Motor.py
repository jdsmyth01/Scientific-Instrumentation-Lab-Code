import numpy as np
import math
import matplotlib.pyplot as plt
import time
def motor_run(bpm):
    f = bpm/120
    l = .88265 #rod length meters
    r = .1 #rod radius
    m1 = .050616 #rod mass kg
    m2 = .3426 #added mass kg
    g = 9.8
    alpha = (1/(2*np.pi*f))**2*(g/l)
    print(alpha*l)
    d = (alpha*l*(m1+m2) - (l/2)*m1)/m2
    print('place mass at %f then press enter' %d)
    input()
    print('a')
motor_run(115)

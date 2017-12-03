# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:49:44 2016
The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the Explicit Euler method, various graphs are plotted and the stability is tested.
The file is preset to use EulerFoward and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constant dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied. Additionally small == False so that small angle approximations are not used.

"""



# This script creates a Oscillator object that starts at rest with an intial angle of 0.75*pi
# If the argument small == False, small angle approxiations are not used.
# The Explicit Euler method is used to solve the equations of motion.

import numpy as np
import ode4
from ode4 import Oscillator
w=Oscillator(numOsc=1,small=False,initial1=[0.75*np.pi,0.0],initial2=[0.1,0.0,0.0,0.0],dHat=0.2) # if dHat is non-zero the pendulum is damped.
w.ExEuler(step=0.05,end=50)
w.plot(v=True, E= True)
w.stability()
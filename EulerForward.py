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
are arguments and can all be varied. 

@author: Corey
"""

import ode4
from ode4 import Oscillator
w=Oscillator(numOsc=1, small=False,initial1=[0.1,0.0],initial2=[0.1,0.0,0.0,0.0],dHat=0.2) # if dHat is non-zero the pendulum is damped.
w.ExEuler(step=0.005,end=50)
w.plot(v=True, E= True)
w.stability()

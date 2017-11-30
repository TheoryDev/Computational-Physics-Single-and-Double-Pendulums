# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 22:21:41 2016

The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the RK4 method, various graphs are plotted and the stability is tested.
The file is preset to use RK4 and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constant dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied. Additionally can set small == False so that small angle approximations are not used.

@author: Corey
"""
# Try for numOsc == 2, (R=0.01,G=0),(R=0.01,=1),(R=1,G=0),(R=1,G=1),(R=100,G=0),(R=100,G=1)
# They produce various results

import ode4
from ode4 import Oscillator
w=Oscillator(numOsc=2, small=False,initial1=[0.1,0.0],initial2=[0.1,0.0,0.0,0.0],dHat=0.2,R=0.01,G=0.) # if dHat is non-zero the pendulum is damped.
w.RK4(step=0.0005,end=100)
w.plot(v=True, E= True)
w.stability()
#print w.E

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 00:01:07 2016
This script creates animations using matplotlib.animate. An Oscillator class object is created.
Then the equations of motions are solved, it is set to use RK4 but this can be
change by the user. Graphs are plotted and so are animations.

@author: Corey
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation
from ode4 import Oscillator 

plt.close()

#Get smaller standard deviation

A=Oscillator(numOsc=2 ,small=False, initial2= [0.35,0.1,0.,0.],R=0.01)
if A.numOsc!= 2:
    raise Exception('The animations only works for a double pendulum numOsc be equal to 2')
A.RK4(end=50,step=0.005)
A.plot(v=True,E=True)
x1,y1 = np.sin(A.theta[:,0]),-np.cos(A.theta[:,0])
x2,y2 = np.sin(A.theta[:,1])+np.sin(A.theta[:,0]),-np.cos(A.theta[:,1])-np.cos(A.theta[:,0])
h=A.h
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2.1, 2.1), ylim=(-2.1, 0.1))
string, = ax.plot([],[],'o-',lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05,0.9,'',transform=ax.transAxes)
def init():
    string.set_data([], [])
    time_text.set_text('')
    return string, time_text

def animate(i):      
    X = [0, x1[i],x2[i]]
    Y = [0, y1[i],y2[i]]
    string.set_data(X,Y)
    time_text.set_text(time_template % (i*h))        
    return string, time_text
ax.grid()        
motion = animation.FuncAnimation(fig,animate,np.arange(1,len(x1)) ,interval=2, blit=True, init_func=init)

plt.show()


## Comparison of numerical ordinary differential equation solvers through pendulum simulations

`The Scripts are best run in the terminal using Python 2`

The scripts are used to model the oscillators and the last script also produces animations.

#  ode4.py:

This module contains the Oscillator class that creates oscillator objects. 
The objects have different methods that provide numerical solutions to the differential equations and also plot graphs.
The oscillators can be either singe or double pendulums.
The Explicit Euler, Implicit Euler, Leapfrog and Fourth-Order Runge-Kutta finite difference numerical methods are all 
class methods that can be called to solve the equations of motion. 
The equations of motions can use small angle approximations or not use small angle approximations.

The initial conditons and step size can be varied.
The stability of the solution can be tested.
Energy can be calculated.

# Description of scripts: 

Each script simulates the motion of a pendulum using the given ODE solver. 
Various graphs are plotted and the stability of the solution is tested.
The file is preset to create a double pendulum but can be changed to use a single pendulum.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, if 'numOsc' == 2 the pendulum is a double pendulum. 
For a single pendulum the scaled damping constant is dHat and the initial conditions are arguments.
For the double pendulum the mass of the first pendulum, `m`, mass Ratio `R`, scaled damping constant `G`, are arguments and can all be varied.  

# There are two special scripts:

EulerForwardArbitary.py: solves differential equations without using small angle approximations by setting the parameter `small` == False.

animations.py: This script creates animations using matplotlib.animate. An Oscillator class object is created.
Then the equations of motions are solved, it is set to use RK4 but this can be
changed by the user. Graphs are plotted and so are animations.

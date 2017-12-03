# Comparison of numerical ordinary differential equation solvers through pendulum simulations

 ### `Diagram of single and double pendulums`
 <p align="center"> 
 <img src="/images/pendulums.png" height= "250" width="250">
 </p>

`The Scripts are best run in the terminal using Python 2. When running animations make sure that the plot is displayed outside of the terminal as it will only show a blank grid if it is show inline.`

The scripts are used to model the oscillators and the last script also produces animations.

#  Module to simulate physics:

`ode4.py` contains the Oscillator class that creates oscillator objects. 
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
If the object is initialized with the `numOsc`== 1 the pendulum is a single pendulum, if `numOsc` == 2 the pendulum is a double pendulum. 
For a single pendulum the scaled damping constant is dHat and the initial conditions are arguments.
For the double pendulum the mass of the first pendulum, `m`, mass Ratio `R`, scaled damping constant `G`, are arguments and can all be varied.  

## There are two special scripts:

EulerForwardArbitary.py: solves differential equations without using small angle approximations by setting the parameter `small` == False.

animations.py: This script creates animations using matplotlib.animate. An Oscillator class object is created.
Then the equations of motions are solved, it is set to use RK4 but this can be
changed by the user. Graphs are plotted and so are animations.

# Sample Outputs

Below are some sample plots showing the angular displacement in various situations and final plot is a graph of the pendulum's energy over time.
<p align="center"> 
<img src="/images/R001G0.png" align="middle" height= "400" width="400"/> <img src="/images/R100G1.png" align="center" height= "400" width="400">
</p>
 
<p align="center"> 
<img src="/images/R1G1.png" align="center" height= "400" width="400"/> <img src="/images/graph1rk4h0dot01.png" align="center" height= "400" width="400">
</p>

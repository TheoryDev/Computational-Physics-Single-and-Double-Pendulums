List of files:
------------------
Modules used to model physics:
ode4.py

-----------------
--------------------
Scripts:
EulerForward.py
EulerForwardArbitary.py
ImplicitEuler.py
Leapfrog.py
RK4.py
animations.py
--------------------
The first module is used to model the physics.

The scripts are used to model the oscillators 
and the last script creates animations.
--------------------------------------------------
Description of ode4 used to model the physics.

The file, ode4.py:

This module contains the Oscillator class that creates oscillator objects. 
The objects have different methods that provide numerical solutions to the differential equations and also plot graphs.
The oscillators can be either singe or double pendulums.
The Explicit Euler, Implicit Euler, Leapfrog and Fourth-Order Runge-Kutta finite difference numerical methods and all 
class methods that can be called to solve the equations of motion. 
The equations of motions can use small angle approximations or not use small angle approximations.

!!! I developed the code to be able use the equations without small angle approximations for all four methods
and for both double and single pendulums !!!

The initial conditons and step size can be varied.
The stability of the solution can be tested.
Energy can be calcualted.

-------------------------------------------------------
Description of scripts.

The file, EulerForward.py:

The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the EulerForward method, various graphs are plotted and the stability is tested.
The file is preset to use EulerFoward and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constand dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied.  

The file, EulerForwardArbitary.py:

The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the Explicit Euler method, various graphs are plotted and the stability is tested.
The file is preset to use EulerFoward and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constand dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied. Additionally small == False so that small angle approximations are not used.

The file, ImplicitEuler.py:

The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the Implicit method, various graphs are plotted and the stability is tested.
The file is preset to use Implicit Euler and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constand dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied. Additionally can set small == False so that small angle approximations are not used.

The file, Leapfrog.py:

The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the Leapfrog method, various graphs are plotted and the stability is tested.
The file is preset to use Leapfrog and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constand dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied. Additionally can set small == False so that small angle approximations are not used.

The file, RK4.py:

The script calls the Oscillator class in ode4.py to create
a class object. The object's equations of motions are then solved by
the RK4 method, various graphs are plotted and the stability is tested.
The file is preset to use RK4 and to create a double pendulum. The number of pendulums can be changed.
If the object is initialized with the numOsc==1 the pendulum is a single pendulum, 
if numOsc==2 the pendulum is a double pendulum. For a single pendulum the scaled damping constand dHat
and the initial conditions are arguments.For the double pendulum the mass of the first pendulum, m, mass Ratio, R, scaled damping constant G,
are arguments and can all be varied. Additionally can set small == False so that small angle approximations are not used.


The file, animations.py:

This script creates animations using matplotlib.animate. An Oscillator class object is created.
Then the equations of motions are solved, it is set to use RK4 but this can be
change by the user. Graphs are plotted and so are animations.
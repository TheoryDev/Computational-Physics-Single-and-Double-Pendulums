# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 12:55:47 2016


This module contains the Oscillator class that creates oscillator objects. 
The objects have different methods that provide numerical solutions to the differential equations and also plot graphs.
The oscillators can be either singe or double pendulums.
The Explicit Euler, Implicit Euler, Leapfrog and Fourth-Order Runge-Kutta finite difference numerical methods and all 
class methods that can be called to solve the equations of motion. 
The equations of motions can use small angle approximations or not use small angle approximations.
The initial conditons and step size can be varied.
The stability of the solution can be tested.
Energy can be calcualted.
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation



class Oscillator: # put in instructions doc string for intial and operator
    """ The Oscillator class creates objects that are initialised with an operator matrix and intial angular displacement and velocity conditions.
        The class objects model both single and double pendulums which can then use the same methods which differntiate between the two cases.
        When a class object is created the numerical ode solver methods solve the differential equations as systems of linear ODE's in matrix form.
        Then various methods can be called to process the data to produce plots or to test for stability.
        The oscillator only solves for the specific single pendulum and double pendulum
    """
    def __init__(self,initial1=[0.1,0.],initial2=[0.1,0.0,0.0,0.0],small = False,numOsc=1,m=1.,R=1.,dHat=0.0,G=0.0): # if the angles are too large small angle approx breaks down
        """ The initialisation for Oscillator class objects. 
        The operator argument is a list which is used as a matrix operator to model the system of linear equations.
        initial is a list containing the inital angular displacemenetns first and then the angular velocities.
        If self.small == True, a small angle approximation is used and it is not used if self.small == False."""
        self.numOsc = numOsc
        self.R = R # mass ratio
        self.m = m
        self.M = self.R*self.m # the mass M scales with the mass m
        if self.numOsc == 1 : # single pendulum
            self.L = np.array([[0.0,1.0],[-1.0,-dHat]],dtype = float)
            if len (initial1) == 2:
                self.x0 = np.array(initial1)
            else:
                raise Exception("For a single pendulum the list containing the initial coordinates must contain two elements")
        if self.numOsc == 2 : #double pendulum
            self.L = np.array( [[0.,0.,1.,0.],[0.,0.,0.,1],[-(R+1.),R,-G,0.],[(R+1.),-(R+1.),G*(1.-1./R),-G/R]])
            if len(initial2) == 4:
                self.x0 = np.array(initial2)
            else:
                raise Exception("For a double pendulum the list containing the initial coordinates must contain four elements")       
        
        self.solved = False # If == True ,class methods know a ode solver has solved the differential equations
        self.solved2 = False # If == True ,class methods know the oscillator system's energy has been calculated
        self.small = small # If == True, small angle approximations are used , if == False, they are not
        if self.small==True:
            print "Small angle approximations will be used"
        if self.small == False:
            print "Small angle approximations will not be used"
        
    def ExEuler(self,start=0.,end=50.,step=0.05):
        """ The ExEuler class method is an Explict Euler numerical ode solver method that works on systems of linear ODE's in marix form. Start is the starting point in time, end is the end point and step is the step size. Note time is in natural units """
        self.solved = True
        self.type = "Explicit Euler" # sets type for use by other class methods
        t= np.arange(start, end, step, dtype = float)     
        self.t = t
        self.h = step
        #self.h = step
        self.theta = np.ones((t.size,len(self.x0)), dtype = float) 
        self.theta[0] = self.x0 # intial angular displacements then velocites
        for i in range(1,t.size):
            if self.small == False: # Without the small angle approximation a few matrix elements must be continually updated.           
                if self.numOsc == 1: 
                   if self.theta[i-1][0] == 0.0: # This is to prevent 0./0. I tried a sinc function but it caused errors.
                       self.L[1][0]== 0.0
                   else:  
                       self.L[1][0] = -np.sin(self.theta[i-1][0])/self.theta[i-1][0]
                if self.numOsc == 2:
                   if self.theta[i-1][0]== 0.0:
                       self.L[2][0]= 0.0
                       self.L[3][0]= 0.0
                   else:   
                       self.L[2][0] = -(self.R+1)*np.sin(self.theta[i-1][0])/self.theta[i-1][0]                    
                       self.L[3][0] = (self.R+1)*np.sin(self.theta[i-1][0])/ self.theta[i-1][0]                   
                   if self.theta[i-1][1]== 0.:
                       self.L[2][1] = 0.0
                       self.L[3][1] = 0.0 
                   else:
                       self.L[2][1] = self.R*np.sin(self.theta[i-1][1])/self.theta[i-1][1]
                       self.L[3][1] = -(self.R+1)*np.sin(self.theta[i-1][1])/self.theta[i-1][1] 
            self.theta[i] = self.theta[i-1] + self.h*self.L.dot(self.theta[i-1]) # estimates next point in time.


    def Leapfrog(self,start=0.,end=50.,step=0.05):
        """ The Leapfrog class method is an leapfrog numerical ode solver that works on systems of linear ODE's in marix form. Start is the starting point in time, end is the end point and step is the step size. Note time is in natural units """
        self.solved = True
        self.type = "Leapfrog"
        t= np.arange(start,end,step, dtype = float)
        h = step
        self.t ,self.h = t,h
        self.theta = np.ones((t.size,len(self.x0)), dtype = float)
        self.theta[0] = self.x0
        self.theta[1] = self.theta[0] + self.h*self.L.dot(self.theta[0])
        for i in range(2,t.size):
            if self.small == False: # Without the small angle approximation a few matrix elements must be continually updated.               
               if self.numOsc == 1:  
                   if self.theta[i-1][0] == 0.0: # This is to prevent 0./0. I tried a sinc function but it caused errors.
                       self.L[1][0]= 0.0
                   else:  
                       self.L[1][0] = -np.sin(self.theta[i-1][0])/self.theta[i-1][0]
               if self.numOsc == 2:
                   if self.theta[i-1][0] == 0.0:
                       self.L[2][0]= 0.0
                       self.L[3][0]= 0.0
                   else:   
                       self.L[2][0] = -(self.R+1)*np.sin(self.theta[i-1][0])/self.theta[i-1][0]                    
                       self.L[3][0] = (self.R+1)*np.sin(self.theta[i-1][0])/ self.theta[i-1][0]                   
                   if self.theta[i-1][1] == 0.0:
                       self.L[2][1] = 0.0
                       self.L[3][1] = 0.0 
                   else:
                       self.L[2][1] = self.R*np.sin(self.theta[i-1][1])/self.theta[i-1][1]
                       self.L[3][1] = -(self.R+1)*np.sin(self.theta[i-1][1])/self.theta[i-1][1] 
            self.theta[i] = self.theta[i-2] + 2*self.h*self.L.dot(self.theta[i-1])  # estimates next point in time.

    def RK4(self,start=0.,end=50.,step=0.05):
        """ The RK4 class method is an Runge-Kutta 4 numerical ode solver that works on systems of linear ODE's in marix form. Start is the starting point in time, end is the end point and step is the step size. Note time is in natural units"""
        self.solved = True
        self.type = "RK4"
        t= np.arange(start,end,step, dtype = float)       
        self.t ,self.h = t,step
        self.theta = np.ones((t.size,len(self.x0)), dtype = float)
        self.theta[0] = self.x0
        c = (1./6.)
        for i in range(1,t.size):            
            if self.small == False:      # Without the small angle approximation a few matrix elements must be continually updated.                          
               if self.numOsc == 1: 
                   if self.theta[i-1][0] == 0.0: # This is to prevent 0./0. returing as Nan, I tried a sinc function but it caused errors.
                       self.L[1][0]= 0.0
                   else:  
                       self.L[1][0] = -np.sin(self.theta[i-1][0])/self.theta[i-1][0]
               if self.numOsc == 2:
                   if self.theta[i-1][0]== 0.0:
                       self.L[2][0]= 0.0
                       self.L[3][0]= 0.0
                   else:   
                       self.L[2][0] = -(self.R+1)*np.sin(self.theta[i-1][0])/self.theta[i-1][0]                    
                       self.L[3][0] = (self.R+1)*np.sin(self.theta[i-1][0])/ self.theta[i-1][0]                   
                   if self.theta[i-1][1]== 0.0:
                       self.L[2][1] = 0.0
                       self.L[3][1] = 0.0 
                   else:
                       self.L[2][1] = self.R*np.sin(self.theta[i-1][1])/self.theta[i-1][1]
                       self.L[3][1] = -(self.R+1)*np.sin(self.theta[i-1][1])/self.theta[i-1][1] 
            k1 = self.h*self.L.dot(self.theta[i-1])
            k2 = self.h*self.L.dot(self.theta[i-1]+0.5*k1)            
            k3 = self.h*self.L.dot(self.theta[i-1]+0.5*k2)
            k4 = self.h*self.L.dot(self.theta[i-1]+k3)
            self.theta[i] = self.theta[i-1] + c*(k1 + 2*k2 + 2*k3+ k4) # estimates next point in time.

    def ImEuler(self,start=0.,end=50.,step=0.05):
        """ The ImEuler class method is an implicit Euler numerical ode solver that works on systems of linear ODE's in marix form. Start is the starting point in time, end is the end point and step is the step size. Note time is in natural units"""
        self.solved = True
        self.type = "Implicit Euler"
        t= np.arange(start,end,step, dtype = float)        
        self.t ,self.h = t, step
        self.theta = np.ones((t.size,len(self.x0)),dtype=float)
        self.theta[0] = self.x0
        if self.numOsc == 1:
            I = np.array([[1.,0.],[0.,1.]]) # Identity matrix
        if self.numOsc == 2:
            I = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]])  #  Indentity matrix    
        for i in range(1,t.size):
            if self.small == False:    # Without the small angle approximation a few matrix elements must be continually updated.                           
                if self.numOsc == 1: 
                   if self.theta[i-1][0] == 0.0: # This is to prevent 0./0. I tried a sinc function but it caused errors.
                       self.L[1][0]= 0.0
                   else:  
                       self.L[1][0] = -np.sin(self.theta[i-1][0])/self.theta[i-1][0]
                if self.numOsc == 2:
                   if self.theta[i-1][0]== 0.0:
                       self.L[2][0]= 0.0
                       self.L[3][0]= 0.0
                   else:   
                       self.L[2][0] = -(self.R+1)*np.sin(self.theta[i-1][0])/self.theta[i-1][0]                    
                       self.L[3][0] = (self.R+1)*np.sin(self.theta[i-1][0])/ self.theta[i-1][0]                   
                   if self.theta[i-1][1] == 0.0:
                       self.L[2][1] = 0.0
                       self.L[3][1] = 0.0 
                   else:
                       self.L[2][1] = self.R*np.sin(self.theta[i-1][1])/self.theta[i-1][1]
                       self.L[3][1] = -(self.R+1)*np.sin(self.theta[i-1][1])/self.theta[i-1][1] 
            T = np.linalg.inv(I-self.h*self.L)   # creates inverse matrix 
            self.theta[i]=self.theta[i-1].dot(T) # estimates next point in time.

    def plot(self,x=True,v= True,E= True):
        """ The class method plot, produces plots of the angular displacements and velocites and also the oscillator energy.
            The plot are produced for a class object for which the equations of motion have already been solved.
            If x == True, angular displacement is plotted, if x == True, angular velocity is plotted, if E == True energy is plotted
        """
        tmp = range(len(self.x0)/2) # number of oscillators
        if self.solved == False:
            raise Exception ("The differential equations must first be solved to provide solutions to plot")
        if self.solved == True:
                if x == True:
                    plt.figure()
                    for i in tmp:
                            if i == 0:
                                j = 1
                                angX = "Theta"
                                #j is used to select the angular displacement from the correct pendulum                    
                            if i == 1:
                                angX = "Phi"
                                j = 2 
                                
                            plt.plot(self.t,self.theta[:,i],'.-', label = angX  +" using " + self.type + " with h=" + str(self.h)) # plots graphs with pendulum number , displacement and step size
                            plt.ylabel ('Angular Displacement')
                            plt.xlabel('Scaled Time')
                            plt.legend()
                if v == True:
                    plt.figure()
                    for i in tmp:
                            if self.numOsc == 1:
                                j=1
                                angV = "thetadot"
                            if self.numOsc == 2:    
                                if i == 0:
                                    j = 2 
                                    angV = "thetadot"                                    
                                    #j is used to select the angular displacement from the correct pendulum      
                                if i == 1:
                                    j = 3
                                    angV = "phidot"

                            plt.plot(self.t,self.theta[:,j],'.-', label = angV   +" using " + self.type + " with h=" + str(self.h)) # plots graph with pendulum number, angle and step size
                            plt.xlabel('Scaled Time')
                            plt.ylabel('Angular Velocity')
                            plt.legend()
                if self.solved2 == False: # Prevents calculating energy if already calculated
                    self.energy() # calls the energy method to calculate the oscillator energy with respect to time.                   
                        
                if E == True:                  
                        plt.figure()
                        plt.plot(self.t,self.E,label="Total energy ")
                        plt.plot(self.t,self.KE,label="Kinetic energy ")
                        plt.plot(self.t,self.PE,label="Potential energy ") 
                        plt.xlabel('Scaled Time')
                        plt.ylabel('Scaled Energy')
                        plt.legend()               # Plots total energy allowing for great visual comparisons of energy conservation  
   
       
    def energy(self,spread=False):
        """ This class method calculates the energy for an oscillator object. 
            The oscillator class object's equations of motions must have already have been solved.
            If spread == True the standard deviation of the energy is calculated, a larger spread indicates greater errors.
            """
        if self.solved == False:
            raise Exception("The differential equations must first be solved to provide solutions to calculate energies")

        if self.solved ==True:
            if self.small == True:
                if self.numOsc == 1:        
                    self.KE = 0.5*self.theta[:,1]*self.theta[:,1] # kinetic energy equation for single pendulum
                    self.PE = 0.5*self.theta[:,0]*self.theta[:,0] # potential energy equation for single pendulum
                    
                    #
                if self.numOsc == 2:
                  
                    self.KE1 = 0.5*self.m*self.theta[:,2]*self.theta[:,2] # kinetic energy equation for first pendulum
                    self.KE2 = 0.5*self.M*((self.theta[:,3]*self.theta[:,3])+self.theta[:,2]*self.theta[:,2]+2*self.theta[:,2]*self.theta[:,3]) # kinetic energy equation for second pendulum
                    self.PE1 = self.m*(0.5*self.theta[:,0]*self.theta[:,0]) # potential energy equation for first pendulum
                    self.PE2 = self.M*(0.5*self.theta[:,0]*self.theta[:,0]+0.5*self.theta[:,1]*self.theta[:,1]) # potential energy equation for second pendulum
                    self.KE, self.PE = (self.KE1+self.KE2), (self.PE1 + self.PE2) 
                
            
            elif self.small == False:   
                 if self.numOsc == 1:        
                    self.KE = 0.5*self.theta[:,1]*self.theta[:,1] # kinetic energy equation for single pendulum
                    self.PE = (1.-np.cos(self.theta[:,0])) # potential energy equation for single pendulum
                    
                   
                 if self.numOsc == 2:
                  
                    self.KE1 = 0.5*self.m*self.theta[:,2]*self.theta[:,2] # kinetic energy equation for first pendulum
                    self.KE2 = 0.5*self.M*((self.theta[:,3]*self.theta[:,3])+self.theta[:,2]*self.theta[:,2]+2*np.cos(self.theta[:,0]-self.theta[:,1])*self.theta[:,2]*self.theta[:,3]) # kinetic energy equation for second pendulum
                    self.PE1 = self.m*(1.-np.cos(self.theta[:,0])) # potential energy equation for first pendulum
                    self.PE2 = self.M*(2.-np.cos(self.theta[:,0])-np.cos(self.theta[:,1])) # potential energy equation for second pendulum
                    self.KE, self.PE = (self.KE1+self.KE2), (self.PE1 + self.PE2) 
                    
            
            else:
                raise Exception('The argument small in the class initilisation must equal boolean values True or False ')
            
            self.E = self.KE+self.PE # total energy of oscillator
            self.spreadE = np.std(self.E) # standard deviation of energy
            self.solved2 = True # Allows other class methods to tell the energy has been calcualted.
        if spread == True:
            print "Standard deviation is  " , self.spreadE 
               

    def stability(self,tolerance= 0.1 ): # make way of knowing if it is damped
        """ This class method tests for the stability using the total energy.     
        tolerance == test tolerence level for percentage difference in energy at time t to initial energy at which the system is declared unstable. 
        The technique uses the law of conservation of energy.
        The energy should not increase with time as the system is not driven.            
        """
        
        self.tests=[] # Will be a list of the difference between each energy at time t and the initial energy
      
        if self.solved == False: 
            raise Exception ("The differential equations must first be solved to provide solutions to check for error")
        if self.solved == True:
            if self.solved2 == False:
                self.energy()
        for i in range(1,len(self.E)):            
            test = (self.E[i]-self.E[0])/self.E[0] # percentage difference in energy       
           
            self.tests.append(test)             
            if test >= tolerance:               
                print "unstable at point number " +str(i) 
                self.worked = False
                break
    
            
        else:
            self.worked = True
            print 'stability test sucessful'      
       
            
   
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# define constants in equation to calculate altitude

G = 2.402E-16 # (km^3)/(kg * min^2)
M = 5.97E24 # kg
R = 6378 # km

# "continue?" variable to control the while loop

cont = 'y'

while cont == 'y':

    T_input = input('Please specify the orbital period of the satellite with units (s, min, hr, or days): ') 

    # split the string into two components of a list to work with
    
    # split method found at https://www.simplilearn.com/tutorials/python-tutorial/split-in-python#:~:text=Whenever%20there%20is
    # %20a%20need,given%20string%20or%20given%20line

    T = T_input.split(" ")
    
    # convert first item of list to a number

    T_eq = float(T[0])

    # unit conversion (if necessary)
    
    if T[1] == "s":
        T_eq = T_eq / 60
    elif T[1] == "hr":
        T_eq = T_eq * 60
    elif T[1] == "days":
        T_eq = T_eq * 1440
    
    # calculate and round the altitude

    h = round((((G*M*(T_eq**2))/(4*(np.pi**2)))**(1/3))-R) # km

    # print out the altitude result from the user's input 
    
    if h > 0:
        print("The altitude is", h, "km")
    else:
        print("This orbit is not possible.")
        
    # allow user to decide to continue or end the program
    
    cont = input("Would you like to try another orbit? Please answer y or n. ")


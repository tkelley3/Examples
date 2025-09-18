#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import array
from numpy import pi

T = array([94, 240, 360, 1440]) # min

G = 2.402E-16 # (km^3)/(kg * min^2)
M = 5.97E24 # kg
R = 6378 # km

h = (((G*M*(T**2))/(4*(pi**2)))**(1/3))-R # km

h.round(0,h) # method found at https://stackoverflow.com/questions/46994426/how-to-round-a-numpy-array

print(T)

print(h)


# In[2]:


## test cases

test = array([120, 480, 2880])

G = 2.402E-16 # (km^3)/(kg * min^2)
M = 5.97E24 # kg
R = 6378 # km

htest = (((G*M*(test**2))/(4*(pi**2)))**(1/3))-R # km

htest.round(0,htest)

print(test)

print(htest)

# tested against hand calculations, all were correct


# In[ ]:





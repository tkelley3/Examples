# -*- coding: utf-8 -*-
"""
Created on ...

@author: ...
Description: ...
    
"""
import numpy as np
def main():
    #Define constants
    G = 6.67*10**(-11)
    M = 5.98*10**(24)
    Re = 6378100
    T = [94.,60*4., 60*6.,24.*60]
    period = np.array(T)
    period = 60*period
    h = (G*M*period**2/(4*np.pi**2))**(1/3)-Re
    #convert to km
    h = h/1000
    h = np.around(h)
    print(f'For satellites to have a period of {T} minutes, they must have an altitude of {h} km')
    return h
#The code below runs whatever is in main()
if __name__ == '__main__':
    main()
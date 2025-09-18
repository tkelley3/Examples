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
    run='y'
    while (run == 'y'):
        period = input("Enter the period of a satellite in minutes: ")
        [T, units] = period.split(' ')
        minperiod= 60*float(T)
        h = (G*M*minperiod**2/(4*np.pi**2))**(1/3)-Re
        #convert to km
        h = h/1000
        h = np.around(h)
        print(f'For satellites to have a period of {T} {units}, they must have an altitude of {h} km')
        run = input('Run again? ')
    return h
#The code below runs whatever is in main()
if __name__ == '__main__':
    main()
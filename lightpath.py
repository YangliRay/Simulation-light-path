# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:52:21 2021
@author: 1229290416
"""

import numpy as np
import matplotlib.pyplot as plt

#Find intercection of two function in given range
def get_intersection(f, g, minimum, maximum):
    mini = minimum
    maxi = maximum
    result = []

    while ((f(mini) == None) and mini < maxi):
        mini = mini + 0.0001

    while ((f(maxi) == None) and mini < maxi):
        maxi = maxi - 0.0001
        
    if mini >= maxi:
        return result
    
    else:
        k = mini
        while k  < maxi:
            if ((f(k)-g(k))*(f(k+0.0001)-g(k+0.0001))) <= 0:
                result.append([k + 0.00005, g(k + 0.00005)])
            else:
                result = result
            k = k + 0.0001
        return result

#Find slope of a function at given point
def get_slop(f, x):
    return ((f(x+0.000000001)-f(x))/0.000000001)

#Ray trace of a light without deflection
def ray(origin, k, x):
    return (k*x + origin)

#Light path with no refraction , stop at the next refraction
def light(O, k_1, mini, maxi, n, f): #
    
    #Ray path
    def g(x):
        return ray(O, k_1, x)

    
    #Intersection between light and lens
    point = get_intersection(f, g, mini, maxi)
    
    #If an intersection exist
    if point != []:
        
        #The first intersection point
        point_x = point[0][0]
        point_y = point[0][1]
    
        #Draw from origin to first intersection
        xx = np.linspace(mini, point_x, 1000)
        plt.plot(xx, g(xx), color = 'blue', linewidth = 0.3)
        
        #Calculate gradient after deflection, using Snell's law
        theta = np.arctan(get_slop(f, point_x))
        theta_prime = np.arctan(k_1)
        theta_2 = np.arcsin( (np.sin( - (np.pi/2) - theta + 
                                        theta_prime ) ) / n)
        
        if n > 1:
            k_2 = np.tan( - ( (np.pi/2) - theta + theta_2 ))
            
        else:
            k_2 = np.tan( - ( (np.pi/2) - theta - theta_2 ))

        #If next interface exist, return the information deflected light
        return [[-k_2 * point_x + point_y, k_2 
                    ,point_x + 0.01, maxi], True]
 
    #If first lens do not exist, draw the light path directly
    else: 
        xx = np.linspace(mini, maxi, 1000)
        plt.plot(xx, g(xx), color = 'blue', linewidth = 0.3)
        return [0, False]

#Light path, auto detection for lens           
def shot(O, k, mini, maxi, p, f):
    
    #Draw the first part of light path
    light(O, k, mini, maxi, p[0], f)
    i = 0
    
    #If exist next interface, countinue drawing
    while light(O, k , mini, maxi, p[i], f)[1] != False:
        
        #Change refractive index of medium
        i = i + 1
        [O, k, mini, maxi] = light(O, k, mini, maxi, p[i-1], f)[0]
        
        #Draw next part
        light(O, k , mini, maxi, p[i], f)
        
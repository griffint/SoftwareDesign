# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: griffin tschurwald

credit to Abe Kim and Moar Bernstein for assistance
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import *

def build_random_function(min_depth, max_depth):
    # your doc string goes here
    """ This produces a functions of depth between min_depth and max_depth. 
    Large numbers will hit max recursion value, and min_depth 
    must be smaller than max depth    
    """
    # your code goes here
    
    #code to generate depth based 
    #max and min
    
        
    #List of functions to be used
    base_list = [['x'],['y']]
    if max_depth <= 1:
        return base_list[randint(0,1)]
    first_optional = build_random_function(min_depth-1,max_depth-1)
    second_optional = build_random_function(min_depth-1,max_depth-1)
    prod = ['prod',first_optional,second_optional]
    cos_pi = ['cos_pi',first_optional]
    sin_pi = ['sin_pi',first_optional]
    squared = ['^2',first_optional]
    cubed = ['^3',first_optional]
    function_list = [prod,cos_pi,sin_pi,squared,cubed,['x'],['y']]
    if min_depth > 1:
        return function_list[randint(0,4)]
    else:
        return function_list[randint(0,6)]
        
        
def evaluate_random_function(f, x, y):
    # your doc string goes here
    """This function will evaluate the random function
    built by build_random_function. The inputs x and y must be between 
    -1 and 1, inclusive.
    """
    # your code goes here

    funcing = f[0]
    if funcing == 'x':
        return x
    if funcing == 'y':
        return y
    if funcing == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if funcing == 'cos_pi':
        return cos(pi*(evaluate_random_function(f[1],x,y)))
    if funcing == 'sin_pi':
        return sin(pi*(evaluate_random_function(f[1],x,y)))
    if funcing == '^2':
        return (evaluate_random_function(f[1],x,y))**2
    if funcing == '^3':
        return (evaluate_random_function(f[1],x,y))**3        
        
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    # your code goes here
    return((float(val)-float(input_interval_start))*(float(output_interval_end)-float(output_interval_start))/(float(input_interval_end)-float(input_interval_start))+float(output_interval_start))
    
def generate_image(width,height):
    

    blue_function = build_random_function(randint(5,7),randint(12,15))
    red_function = build_random_function(randint(4,7),randint(8,15))
    green_function = build_random_function(randint(5,6),randint(9,15))
    print blue_function
    print red_function
    im = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            b = int(evaluate_random_function(blue_function, remap_interval(i,0,width,-1,1), remap_interval(j,0,height,-1,1)))
            b = int(remap_interval(b, -1,1,0,235))
            r = int(evaluate_random_function(red_function, remap_interval(i,0,width,-1,1), remap_interval(j,0,height,-1,1)))
            r = int(remap_interval(r, -1,1,0,235))
            g = int(evaluate_random_function(green_function, remap_interval(i,0,width,-1,1), remap_interval(j,0,height,-1,1)))
            g = int(remap_interval(g, -1,1,0,235))
            
            im.putpixel((i,j),(r,g,b))
    im.save("coolpic.bmp")
    
    
    
    
if __name__=='__main__':
    generate_image(350,350)
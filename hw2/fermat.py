# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:57:18 2014

@author: griffin tschurwald
"""

def check_fermat(a,b,c,n):
    if a**n + b**n == c**n:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
input_a = int(raw_input("please input a"))
input_b = int(raw_input("please input b"))
input_c = int(raw_input("please input c"))
input_n = int(raw_input("please input n"))
        
check_fermat(input_a,input_b,input_c,input_n)


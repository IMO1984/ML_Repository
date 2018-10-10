# -*- coding: utf-8 -*-
"""
Scope of variables in python

@author: 
    130873
    Created on Mon Aug  6 15:50:14 2018
"""

count = 0

def show_count():
    print('Count: ',count)

def set_count(c):
    global count
    count = c
    


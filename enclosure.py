# -*- coding: utf-8 -*-
"""Understanding local function and closure
Created on Tue Aug 28 18:45:29 2018

@author: 130873
"""

def outer(x):
    double = x**2
    
    def inner(y):
        return double+y
    
    return inner

def raise_to(exp):
    def raise_to_power(x):
        return pow(x,exp)
    return raise_to_power

import time 

def make_timer():
    last_called = None
    
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        elapsed_time = now - last_called
        last_called = now
        return elapsed_time
    return elapsed



if __name__ == '__main__':
    inf = outer(10)


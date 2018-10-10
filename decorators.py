# -*- coding: utf-8 -*-
"""Understanding decorators
Created on Tue Aug 28 18:45:29 2018

@author: 130873
"""

def escape_unicode(f):   #Function decorator
    def wrap(*args,**kwargs):
        x = f(*args,**kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def text_nascii():
    return "LeoñärdÓ"

class CallCount(): # class decorator
    def __init__(self,f):
        self.count = 0
        self.f = f
    def __call__(self,*args,**kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print("Hello {}".format(name))
    
    
class Trace():
    def __init__(self):
        self.enabled = True
    
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.enabled:
                print("calling {}".format(f))
            return f(*args, **kwargs)
        return wrap
    
tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


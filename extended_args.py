# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:41:32 2018

@author: 130873
"""

def hypervolume(*args):
    args_iterator = iter(args)
    try:
        value = next(args_iterator)
    except StopIteration:
        raise TypeError
    
    for arg in args_iterator:
        value *= arg
    return value

def hypervolume1(arg,*args):
    value = arg
    print(type(args)) # type of args is a tuple
    for arg in args:
        value *= arg
    return value

def hypervolume2(**kwargs):
    print(type(kwargs)) # type of key word args is dict
    result = 1
    for key, value in kwargs.items():
        print("{k} = {v}".format(k=key,v=value))
        result *= value
    return(result)
        
#allowed format for passing arguments
#def function(arg1,      #--> regular positional arguments
#             *args,     #--> arguments list
#             kwarg1,    #--> mandatory kwargs
#             **kwargs)  #--> key word argument list      
#        
    

if __name__ == '__main__':
#    print(hypervolume(3))
#    print(hypervolume(3,4))
#    print(hypervolume(3,4,5))
#    print(hypervolume(3,4,5,6))
#    print(hypervolume())
#    
#    print(hypervolume1(3))
#    print(hypervolume1(3,4))
#    print(hypervolume1(3,4,5))
#    print(hypervolume1(3,4,5,6))
#    print(hypervolume1())
    
    print(hypervolume2(height=10,length=10,width=10))
    
# -*- coding: utf-8 -*-
"""
A module to demonstrating exceptions.

@author: 
    130873
    Created on Tue Aug  7 12:34:19 2018
    
usage:
    this module receive string and retrun the integer after conversion.
    
"""

import sys
from math import log


def convert(s):
    """
    Converts a string to an integer.
    Args:
        receive argument s - any string
        
    returns:    
        returns integer x
    
    """
    
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print("conversion error! {} "\
              .format(str(e)), 
              file =sys.stderr)
        return -1 #raise #return -1 more pythonic handling of exception is to raise 
    
    
def string_log(s):
    """
    Converts a string to an integer.
    Args:
        receive argument s - any string
        
    returns:    
        returns log value
    
    """
    v = convert(s)
    return log(v)
    


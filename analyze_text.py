# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:30:21 2018

@author: 130873
"""

def analyze_text(filename):
    """ return the number of line and charatcter in a file.
    Args:
        filename: Name of the file to analyze
    
    Raises:
        IOError: If 'filename' does not exist or cant't be read"
    
    Returns:A Tuple where the first element is the number of line present in 
    the file and the second element is the number of charaters present 
    in the file
    """
    lines = 0
    chars = 0
    with open(filename,mode='rt',encoding='utf-8') as f:
        for line in f:
            lines += 1
            chars += len(line)
            
    return (lines,chars)
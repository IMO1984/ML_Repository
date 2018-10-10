# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:28:54 2018

@author: 130873
"""
import sys

def int_to_bytes(i):
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff
                ))
    
if __name__ == "__main__":
    b = int_to_bytes(int(sys.argv[1]))
    print(b)
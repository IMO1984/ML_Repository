# -*- coding: utf-8 -*-
"""Demostrating File handling in Python
Created on Mon Aug 13 15:12:23 2018

@author: 130873
"""

import sys
from itertools import count, islice

def sequence():
    """ generate raceman's sequence """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c
        
def write_seq(filename,num):
    """ Write raceman's sequence to a file """
#    f = open(filename,mode = 'wt', encoding='utf-8')
#    f.writelines("{0}\n".format(r)    
#                 for r in islice(sequence(),num+1))
#    f.close()
    with open(filename, mode='wt',encoding='uft-8') as f:
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(),num+1))
    

def read_seq(filename):
#    try:
#        f = open(filename, mode='rt',encoding='utf-8')
#        return [int(line.strip()) for line in f]
#    finally:
#        f.close()
    #using with context manager files get closed on completion automatically
    #and the code is equivalent to the one above
    with open(filename, mode='rt',encoding='uft-8') as f:
        return [int(line.strip()) for line in f]
    

def main(filename,mode,num=0):
#    f = open(filename, mode='rt',encoding='utf-8')
#    for line in f:
#        sys.stdout.write(line)
#    f.close()
    if mode == "write":
        write_seq(filename,num)
        
    if mode == "read":
        series = read_seq(filename)
        print(series)
        
    if mode != "write" and mode != "read":
        print("Invalid file operation mode {}".format(mode))       

    
if __name__ == '__main__':
    main(filename=sys.argv[1],num=sys.argv[2])


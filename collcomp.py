# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:00:09 2018

@author: 130873
"""
from math import sqrt
from pprint import pprint as pp

def listComp(x):
    """Generate square of numbers using list comprehension"""
    sqr_list = [i*i for i in range(x) if isPrime(i)]
    return sqr_list


def dictComp(square_list):
    even_sqrd_dict = {int(sqrt(item)):item for item in square_list\
                      if isEven(item)}
    return even_sqrd_dict


def setComp(square_list):
    length_set = {len(str(item)) for item in square_list}
    return length_set


def tupleComp(n):
    cube_tuple = (x*x*x for x in range(n) if not isEven(x))
    return cube_tuple
    

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isEven(n):
    if n<= 0:
        return False
    if n % 2 == 0:
        return True
    return False

def main():
    x = int(input("Please provide the range:"))
    
    square_list = listComp(x)
    print("Square of prime numbers in range {} is {}".format(x,square_list))
    
    square_dict = dictComp(square_list)
    pp("Even squared of prime numbers in range {} is {}".\
          format(x,square_dict))
    
    length_set = setComp(square_list)
    print("length of generated squared prime numbers in range {} is {}".\
          format(x,length_set))
    
    cube_tuple = tupleComp(x)
    print("cube of odd numbers in range {} is {}:".format(x,cube_tuple))
    
    for cube in cube_tuple:
        print(cube)
    


if __name__ == "__main__":
    main()
    

        
    
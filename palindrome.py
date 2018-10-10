# -*- coding: utf-8 -*-
"""This function cheks if a given number is palindrome or not.

Created on Fri Aug 17 15:14:03 2018

@author: 130873
"""

import unittest


def digits(num):
    """ Converts an integer into list of digits.
    
    Args: 
        num: The number whose digits we want.
    
    Returns:
        A list of digits, in order of 'x'
    
    >>> digits(456789)
    [9, 8, 7, 6, 5, 4]
    """
    digs = []
    while num != 0:
        div,mod = divmod(num,10)
        digs.append(mod)
        num = div
    return digs

def is_palindrome(num):
    """Determine if given number is a plaindrome or not
    
    Args:
        num: The number in question
        
    Returns: True if the number is palindrome. Otherwise False.
    
    >>> is_palindrome(1234)
    False
    
    >>> is_palindrome(12321)
    True
    """
    digs = digits(num)
    for f,r in zip(digs,reversed(digs)):
        if f != r:
            return False
        else:
            return True
     
class Tests(unittest.TestCase):
    """Tests for the is_palindrome function"""
    def test_negetive(self):
        """Test if it return Flase correctly"""
        self.assertFalse(is_palindrome(1234))
        
    def test_positive(self):
        """Test if it return True correctly"""
        self.assertTrue(is_palindrome(1234321))
        
    def test_single_digit(self):
        """Test if it works on single digit numbers too"""
        import pdb;pdb.set_trace()
        for i in range(1,10):
            self.assertTrue(is_palindrome(i))
        
        
#if __name__ == '__main__':
#    unittest.main()
    
#     """to use doctest from inside the module please use the below lines"""
#    import doctest
#    doctest.testmod(verbose=True)
    
    


# -*- coding: utf-8 -*-
"""
Understanding how generator works
Created on Thu Aug  9 14:06:55 2018

@author: 130873
"""


def take(count,iterable):
    """
    Take item from the front of an iterable.
    
    Args:
        count: The maximum number of item to retrieve
        iterable: The source series.
    
    Yields:    
        At most 'count' item from iterable
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item
        
        
def distinct(iterable):        
    """Returns unique elements by eliminating duplicates.
    
    Args: 
        Iterable: The source series.
        
    Yields:
        Unique elements from source iterable.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    """Invoke distinct function and prepare unique elements
    """
    items = [2,3,3,6,6,8,2]
    for item in distinct(items):
        print(item)


def run_take():        
    items = [2,4,6,8,10, ]
    for item in take(3,items):
        print(item)
        
if __name__ == "__main__":
    run_distinct()
            


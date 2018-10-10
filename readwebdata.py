# -*- coding: utf-8 -*-
"""
Retrieve and print words from an URL

@author: 
    130873. Created on Fri Aug  3 18:22:40 2018

Usage:
    python3 readwebdata.py
"""
import sys
from urllib.request import urlopen

def loadWords(wiki_url):
    """Read words from webpage of a given url and 
    return the list of words present in it. 
    
    Args:
        wiki_url: The URL of a wiki topic or any other webpage
        
    Returns:
        A list of words from that webpage
    """
    topic_words = []
    with urlopen(wiki_url) as topic:
        for line in topic:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                topic_words.append(word) 
    return topic_words
                
def fetchItems(item_list,n):
    """This function accepts any iterables and return number of items 
    from that list based on users input.
    
    Args:
        item_list: Any iterable object like list or strings.
        n: an integer to return that many items from the iterable.
        
    Returns:
        None
    """
    for item in item_list[:n]:
        print(item)
        
def main(url):
    """This the the main function which accepts URL as input and 
    then return the words from that webpage based on user input.
    
    Args:
        url: The URL of any webpage
    """
    topic_words = loadWords(url)
    n = int(input('How many words you would like to fetch?'))
    fetchItems(topic_words,n)
            
        
if __name__ == '__main__':
    main(sys.argv[1])   # the 0th arg is the module file name
            
                
        

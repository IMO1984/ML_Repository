# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:50:57 2018

@author: 130873
"""

import socket

class Resolver():
    
    def __init__(self):
        self._cache = {}
    
    
    def __call__(self,host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
    
    def clear(self):
        self._cache.clear()
        
    def has_host(self,host):
        return host in self._cache
    
if __name__ == '__main__':
    resolve = Resolver()
    
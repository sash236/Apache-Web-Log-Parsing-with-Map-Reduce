#!/usr/bin/env python
'''
@author: 
'''

import sys

#Iterate through every line passed in to stdin
for input in sys.stdin.readlines():
#for input in sys.stdin:
    value = input.strip()
    
    print value

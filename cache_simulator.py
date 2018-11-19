import sys
import numpy as np
import pandas as pd

def processCacheFile():
    associtivity = 0
    ways = 16 # size of page/frame table
    size = 10 # number of offset bits
    access_time = 1
    
    with open(sys.argv[1], 'r') as cache_file:
        for line in cache_file:
            x = line.split()
            x[0] = x[0][:-1]
            print(x[0], x[1], x[2], access_time)
            
            access_time += 1
            
processCacheFile()
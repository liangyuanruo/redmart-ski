#!usr/bin/python

import numpy as np
from map import Map
from path import Path

def main():

    m = Map("map.txt")
    m.print_mapFilePath()
    m.print_mapSize()
    m.print_mapArray()

    p = Path()
    print p.find_peaks(m)
    return
    
if __name__ == "__main__":
    main()

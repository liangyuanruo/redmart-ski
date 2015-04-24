#!/usr/bin/python

import numpy as np

class Map:
#Map class to store 2D array of map
   
    #mapFilePath = None
    #mapSize = None
    #mapArray = None
    
    def __init__( self, mapFilePath ):
        self.mapFilePath = mapFilePath
        self.mapSize = self.create_mapSize(mapFilePath)
        self.mapArray = self.create_mapArray(mapFilePath)
        return

    def create_mapSize(self, mapFilePath):
        with open(mapFilePath) as f:
            mapSizeStr = f.readline() #Read first row as string
        #return size as numpy array
        return np.fromstring(mapSizeStr, dtype=int, sep=" ")

    def create_mapArray(self, mapFilePath):
        return np.loadtxt(fname=mapFilePath, skiprows=1, ndmin=2, dtype=int)

    def print_mapFilePath( self ):
        print "Map Filepath: " + str(self.mapFilePath)
        return

    def print_mapSize( self ):
        print "Map Size: " + str(self.mapSize)
        return
    
    def print_mapArray( self ):
        print "Map: \n" + str(self.mapArray)
        return
    
    def get_height( self, pt ):
        return self.mapArray[pt[0]][pt[1]]
   

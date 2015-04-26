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
    
    def move(self, pt, direction):
        #pt is a nparray of [row. col]
        #direction N, S, E or W
        if direction=='N':
            return pt + np.array([-1,0])
        elif direction=='S':
            return pt + np.array([+1,0])
        elif direction=='E':
            return pt + np.array([0,+1])
        elif direction=='W':
            return pt + np.array([0,-1])

        return pt
   

    def get_path( self, startPt, dirTuple ):

        #Starting height
        pt = startPt
        path = ( self.get_height( pt ), )

        #Append new height by following the tuple of directions
        for d in dirTuple:
            pt = self.move( pt, d ) #Get next point
            path = path + ( self.get_height( pt ), )

        return path
    
    
    
    
    
    
    
        

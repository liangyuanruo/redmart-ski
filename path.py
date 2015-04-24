#!/usr/bin/python

import numpy as np

class Path:
#Helper class for Pathfinding

    #Updates coordinates of a point
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

    #Check if a point is within bounds
    def within_bounds(self, mapobj, pt):
        
        #mapobj: Instance of Map class
        #pt: nparray of or [row, col]
        
        mapSize = mapobj.mapSize

        if ( pt[0] < 0 or 
             pt[0] >= mapSize[0] or
             pt[1] < 0 or
             pt[1] >= mapSize[1] ):
            return False
        return True

    #Compare to heights in the map
    def is_lower(self, mapobj, pt1, pt2):
    #Returns true if height of pt1 is lower than pt2
    #Returns false otherwise
        if ( mapobj.get_height(pt1) < 
             mapobj.get_height(pt2) ):
             
            return True
        return False
    
    #Compare to heights in the map
    def height_diff(self, mapobj, pt1, pt2):
    #Returns height difference between pt1 and pt2
        return mapobj.get_height(pt1) - mapobj.get_height(pt2)

    #Helper function to detect peaks
    def is_peak(self, mapobj, pt):
        
        #Check if North is lower
        n_pt = self.move(pt,'N')
        s_pt = self.move(pt,'S')
        e_pt = self.move(pt,'E')
        w_pt = self.move(pt,'W')

        #Check every direction
        if ( #North
             self.within_bounds(mapobj, n_pt) and
             self.is_lower(mapobj, n_pt, pt ) and
             #South       
             self.within_bounds(mapobj, s_pt) and
             self.is_lower(mapobj, s_pt, pt ) and
             #East
             self.within_bounds(mapobj, e_pt) and
             self.is_lower(mapobj, e_pt, pt ) and
             #West
             self.within_bounds(mapobj, w_pt) and
             self.is_lower(mapobj, w_pt, pt )
            ):
            return True
               
        return False
    
    #Helper function to detect troughs
    def is_trough(self, mapobj, pt):
        
        #Check if North is lower
        n_pt = self.move(pt,'N')
        s_pt = self.move(pt,'S')
        e_pt = self.move(pt,'E')
        w_pt = self.move(pt,'W')

        #Check every direction
        if ( #North
             self.within_bounds(mapobj, n_pt) and
             not self.is_lower(mapobj, n_pt, pt ) and
             #South       
             self.within_bounds(mapobj, s_pt) and
             not self.is_lower(mapobj, s_pt, pt ) and
             #East
             self.within_bounds(mapobj, e_pt) and
             not self.is_lower(mapobj, e_pt, pt ) and
             #West
             self.within_bounds(mapobj, w_pt) and
             not self.is_lower(mapobj, w_pt, pt )
            ):
            return True
               
        return False

    #Find peaks in the Map
    def find_peaks(self, mapobj):
        peakList = []

        MAX_ROW, MAX_COL = mapobj.mapSize[0], mapobj.mapSize[1]

        #For the whole map
        for i in range(0,MAX_ROW):
            for j in range(0,MAX_COL):

                pt = np.array([ i, j]) #Create a point

                if self.is_peak(mapobj, pt):
                    #Append every peak to 2D array
                    peakList.append(pt)

        return peakList

   #Recursive depth-first search
   def find_longest_path(self, mapobj, pt):
        #Function returns maximum possible depth
        #that can be traversed from this point
        
        maxDrop = 0
        maxDir = None
        dropDict = {} #Store results from exploring each direction

        if self.is_trough(mapobj, pt):
            return 0 #Can't go anywhere else from here

        #Try to explore north
        if ( within_bounds(self, mapobj, move(pt,'N') and 
               is_lower(mapobj, move(pt,'N'),pt) ):
            dropDict["N"] = find_longest_path(self, mapobj, move(pt,'N'))
            
         

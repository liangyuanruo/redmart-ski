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

        for d in ('N','S','E','W'):
            dirPt = self.move(pt,d)
            if self.within_bounds(mapobj, dirPt):
                if self.height_diff(mapobj, dirPt, pt) > 0:
                    return False
        return True
    
    #Helper function to detect troughs
    def is_trough(self, mapobj, pt):
        
        for d in ('N','S','E','W'):
            dirPt = self.move(pt,d)
            if self.within_bounds(mapobj, dirPt):
                if self.height_diff(mapobj, dirPt, pt) < 0:
                    return False
        return True

    #Find peaks in the Map
    def find_peaks(self, mapobj):
        peakList = []

        MAX_ROW, MAX_COL = mapobj.mapSize[0], mapobj.mapSize[1]

        #For the whole map
        for i in range(0,MAX_ROW):
            for j in range(0,MAX_COL):

                pt = np.array([ i, j ]) #Create a point

                if self.is_peak(mapobj, pt):
                    #Append every peak to 2D array
                    peakList.append(pt)

        return peakList

   #Recursive depth-first search from a point on the map
    def find_longest_path(self, mapobj, pt):
        #Function returns maximum possible depth
        #that can be traversed from this point     
        #Input: Map, Current Point
        #Output: List of steps to take, drop at every step

        temp, stepResult, stepHeightDiff = {},{},{}

        #print "pt="+str(pt)
        #print "self.istrough()="+str(self.is_trough(mapobj,pt))
        
        if ( self.is_trough(mapobj,pt) ):
            return ((),()) # (Drop, Direction) 


        #Try to explore each direction
        for stepDir in ('N','S','E','W'):

            #If direction is lower than current step
            if ( self.within_bounds( mapobj, self.move(pt,stepDir) ) and
                 self.height_diff(mapobj, self.move(pt,stepDir), pt) < 0):

                #Find out what is total drop in that direction dir = height_diff + find_longest path
                stepResult[stepDir] = self.find_longest_path( mapobj, self.move( pt,stepDir ) ) #e.g. ((1,2),('N','E'))
                stepHeightDiff[stepDir] = self.height_diff( mapobj, pt, self.move( pt,stepDir ) ) #Integer
                temp[stepDir] =  ( len(stepResult[stepDir][0]) + 1, sum(stepResult[stepDir][0]) ) #Store total length & drop in each dir
                
        
        #Get best direction (k-v pair)
        #maxDir = max(temp, key=temp.get)
        maxDir = self.get_best_choice(temp)

        #Append drop and direction to the return value of recursive call
        dropTuple = (stepHeightDiff[maxDir],) + stepResult[maxDir][0]
        dirTuple = (maxDir,) + stepResult[maxDir][1] 

        return (dropTuple, dirTuple)


    def get_best_choice(self, temp):
        bestDir, bestLen, bestDrop = None, None, None

        for k,v in temp.iteritems():
            pathLen = v[0]
            pathDrop = v[1]
            
            if pathLen >= bestLen and pathDrop > bestDrop:
                    bestDir = k
                    bestLen = pathLen
                    bestDrop = pathDrop

        return bestDir


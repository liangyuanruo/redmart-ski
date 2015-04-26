#!usr/bin/python

import numpy as np
from map import Map
from path import Path

MAPFILE = "map.txt"

def main():

    print "Loading ", MAPFILE
    m = Map(MAPFILE)

    print "Loading Path library"
    p = Path()

    #Find list of peaks to start searching from
    print "Finding peaks..."
    peaks = p.find_peaks(m)

    print "Searching for best ski slope..."
    maxDict = dict.fromkeys(["startPoint","totalDrop","pathLen","dropTuple","dirTuple"], None)
    
    #Find peak with greatest path
    for pt in peaks:
        
        #Get list of drops, list of directions
        tempDropTuple, tempDirTuple = p.find_longest_path( m, pt )
        
        tempTotalDrop = sum(tempDropTuple) #Calc total drop from list
        tempPathLength = len(tempDirTuple) + 1 #Calc length of path

        #Debugging
        #print "------"
        #print "pathLen="+str(tempPathLength)
        #print "totalDrop="+str(tempTotalDrop)
        #print "startPt="+str(pt)
        #print "startHeight="+str(m.get_height(pt))
        #print "dropTuple="+str(tempDropTuple)
        #print "dirTuple="+str(tempDirTuple)
        #print "path="+str(m.get_path(pt, tempDirTuple))

        #If a new maximum is found, update record
        if maxDict["pathLen"] <= tempPathLength and maxDict["totalDrop"] < tempTotalDrop:
            maxDict["startPoint"] = pt
            maxDict["totalDrop"] = tempTotalDrop
            maxDict["pathLen"] = len(tempDirTuple) + 1
            maxDict["dropTuple"] = tempDropTuple
            maxDict["dirTuple"] = tempDirTuple
        
    print "Done.\n"
    maxDict["path"] = m.get_path( maxDict["startPoint"], maxDict["dirTuple"] )

    #Print results
    print 'Results:'
    for key in maxDict:
        print key, ':', maxDict[key]
    
    return
    
if __name__ == "__main__":
    main()

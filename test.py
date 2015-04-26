
        #Try to explore south
        if ( within_bounds(self, mapobj, move(pt,'S') and 
               is_lower(mapobj, move(pt,'S'),pt) ):

            dropDict['S'] = height_diff(mapobj, pt, move(pt,'S')) + \
                 find_longest_path(self, mapobj, move(pt,'S'))

import numpy as np
import matplotlib.pyplot as plt
from ConvexFinder import findConvex
   
def convertToVertex(convertHull):
    # Converting convex points into vertexes
    convertedHull = np.empty((0,2,2), int)

    # Iterating through each points and creating new vertex
    # Each vertex created by two consecutive convex points
    # Convex points already sorted from 'findConvex' algorithm
    for i in range(1,len(convertHull)):
        newHull = np.empty((0,2), int)
        newHull = np.append(newHull, [[convertHull[i-1][0], convertHull[i][0]]], axis=0) 
        newHull = np.append(newHull, [[convertHull[i-1][1], convertHull[i][1]]], axis=0) 

        convertedHull = np.append(convertedHull, [newHull], axis=0)
    
    # Connecting the first and last points into vertex
    newHull = np.empty((0,2), int)
    newHull = np.append(newHull, [[convertHull[i][0], convertHull[0][0]]], axis=0) 
    newHull = np.append(newHull, [[convertHull[i][1], convertHull[0][1]]], axis=0) 
    convertedHull = np.append(convertedHull, [newHull], axis=0)
    
    return convertedHull

def main(bucket):
    # Main Algorithm
    print("\nFinding ConveExes...")
    bucket = bucket[bucket[:, 0].argsort()]
    convex = findConvex(bucket[0], bucket[-1], bucket, 2)
    print("Finished")

    return convertToVertex(convex)




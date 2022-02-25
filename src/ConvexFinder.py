from DivideAndConquer import *

def findConvex(leftPoint, rightPoint, bucket, choice):
    # Main Algorithm for Convex Hull

    # Based on left and right point, seperating other points into upper and lower parts
    upperBucket, lowerBucket = divide(leftPoint, rightPoint, bucket)

    # Reccursively finds the upper convex points if needed (based on choice)
    upperConvex = np.empty((0,2), int)
    if (upperBucket.size != 0 and choice != 1):
        midPoint = farthestPoint(leftPoint, rightPoint, upperBucket)
        upperConvex = np.array([midPoint])
        upperConvex = np.insert(upperConvex, 0, findConvex(leftPoint, midPoint, upperBucket, 0), axis=0)
        upperConvex = np.append(upperConvex, findConvex(midPoint, rightPoint, upperBucket, 0), axis=0)
    
    # Reccursively finds the lower convex points if needed (based on choice)
    lowerConvex = np.empty((0,2), int)
    if (lowerBucket.size != 0 and choice != 0):
        midPoint = farthestPoint(rightPoint, leftPoint, lowerBucket)
        lowerConvex = np.array([midPoint])
        lowerConvex = np.append(lowerConvex, findConvex(leftPoint, midPoint, lowerBucket, 1), axis=0)
        lowerConvex = np.insert(lowerConvex, 0, findConvex(midPoint, rightPoint, lowerBucket, 1), axis=0)

    if (choice == 0):
        # Finding upper convex
        return upperConvex
    elif (choice == 1):
        # Finding lower convex
        return lowerConvex
    else:
        # Finding both upper and lower convex and also inclusing left and right poiint
        convex = np.array([leftPoint])
        convex = np.append(convex, upperConvex, axis = 0)
        convex = np.append(convex, [rightPoint], axis = 0)
        convex = np.append(convex, lowerConvex, axis = 0)
        return convex
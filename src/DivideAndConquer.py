import numpy as np

def farthestPoint(leftPoint, rightPoint, bucket):
    # Finding the farthest point from vertex (leftPoint, rightPoint)

    # Initiating Values
    maxDist = 0
    maxAngle = 0
    iConvexPoints = 0

    # Iterting through each points
    for i in range(len(bucket)):

        # Calculating distance using cross product
        dist = np.linalg.norm(np.cross(rightPoint-leftPoint, leftPoint-bucket[i]))/np.linalg.norm(rightPoint-leftPoint)

        # Comparing the distances
        if (maxDist < dist):
            # Calculating angle using cosine rules
            cosineAngle = 0.5 * np.dot(bucket[i] - leftPoint, rightPoint-bucket[i]) / (np.linalg.norm(bucket[i] - leftPoint) * np.linalg.norm( rightPoint-bucket[i]))
            maxAngle = np.arccos(cosineAngle)
    
            maxDist = dist
            iConvexPoints = i

        # Comparing angles
        elif (maxDist == dist):
            # Calculating angle using cosine rule
            cosineAngle = 0.5 * np.dot(bucket[i] - leftPoint, rightPoint-bucket[i]) / (np.linalg.norm(bucket[i] - leftPoint) * np.linalg.norm( rightPoint-bucket[i]))
            angle = np.arccos(cosineAngle)

            if (maxAngle < angle):
                iConvexPoints = i
                maxAngle = angle

    return bucket[iConvexPoints]
        
def isLeftSide(p1, p2, pc):
    # Checking which side the compared point is

    # (p1, p2) is the vertex
    # pc is the comparing point

    # Calculation is based on Class's PPT
    compareMatrix = np.array([  [p1[0], p1[1], 1],
                                [p2[0], p2[1], 1],
                                [pc[0], pc[1], 1]])

    det = np.linalg.det(compareMatrix)
    
    return det > 0

def divide(leftPoint, rightPoint, bucket):
    # Main algorithm for Points Divider
    upperBucket = np.empty((0,2), int)
    lowerBucket = np.empty((0,2), int)
    
    # Iterates through each points
    for i in range(len(bucket)):
        # Avoid comparing two same points
        if all(bucket[i] == leftPoint) or all(bucket[i] == rightPoint):
            continue

        # Checking points if it's on the left or right side
        if (isLeftSide(leftPoint, rightPoint, bucket[i])):
            upperBucket = np.append(upperBucket, [bucket[i]], axis=0)
        else:
            lowerBucket = np.append(lowerBucket, [bucket[i]], axis=0)

    return upperBucket, lowerBucket

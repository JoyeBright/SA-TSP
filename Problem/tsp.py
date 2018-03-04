# TSP
# Traveling Saleman Problem
# Implemented by Javad PourMostafa#
# Contact: Javad.PourMostafa@Gmail.com#
#..........................................................................
#..........................................................................

import random as ran
import numpy as num
import math
import collections

def main(xMin,xMax,yMin,yMax,xySize):


    x = ran.sample(range(xMin,xMax),xySize)
    y = ran.sample(range(yMin,yMax),xySize)
    n = len(x)
    d = num.zeros([n,n],dtype=int)

    for i in range(0,n-1):
     for j in range(i+1,n):
         d[i,j] = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
         d[j,i] = d[i,j]

    #print("Distance Matrix:\n %s \n %d*%d Matrix "%(d,n,n))
    #Point = collections.namedtuple('Point',['xMin','xMax','yMin','yMax','x','y','n','d'])
    #p = Point(xMin,xMax,yMin,yMax,x,y,n,d)
    #return p
    # Main(0,100,0,100,15)
    # Main(0,100,0,100,15)[0] = 0
    # Main(0,100,0,100,15)[5] = Distance Matrix

    return {'xMin': xMin, 'xMax': xMax, 'yMin': yMin, 'yMax': yMax, 'x': x, 'y': y, 'n': n, 'd': d}

def ran_permutaive_solution(n):
    return num.random.permutation(n)

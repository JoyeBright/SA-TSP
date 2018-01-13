from MetaHeuristics.Problem.tsp import main,ran_permutaive_solution
import numpy as num

def objective_func(tour,tsp):
    #TourLength

    n = len(tour)
    tour =num.append([tour],tour[0])
    #print("Random Tour:\n",tour)
    L = 0;

    for k in range(0,n):
     i = tour[k]
     j = tour[k+1]
     L = L+ tsp['d'][i,j]
    return L

#objective_func(sol,tsp) which shows tourLength
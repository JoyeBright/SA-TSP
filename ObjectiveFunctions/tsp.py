from MetaHeuristics.Problems.tsp import main,ran_permutaive_solution
import numpy as num

tsp = main(0, 100, 0, 100, 15)
sol = ran_permutaive_solution(tsp['n'])

def objective_func(tour,tsp):
    #TourLength

    n = len(tour)
    tour =num.append([tour],tour[0])
    print("Random Tour:\n",tour)
    L = 0;

    for k in range(0,n):
     i = tour[k]
     j = tour[k+1]
     L = L+ tsp['d'][i,j]
    return L

print("Tour Length:%d"%(objective_func(sol,tsp)))
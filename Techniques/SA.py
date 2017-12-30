from MetaHeuristics.Problems.tsp import ran_permutaive_solution,main
from MetaHeuristics.ObjectiveFunctions.tsp import objective_func
from MetaHeuristics.Neighborhood.swap import swap
import numpy as num
import math as m
import random as ran
#--------------------------------------------------
#Problem Specification
#--------------------------------------------------
MaxIt = 1000  # Maximum Number of Iteration
T0 = 100  # Initial Temp.
alpha = 0.99  # Temp. Reduction Rate
MaxSubIt = 10  # Maximum Number of Sub-Iteration
#--------------------------------------------------
#Create initial Solution
#--------------------------------------------------
tsp = main(0, 100, 0, 100, 15)
sol = ran_permutaive_solution(tsp['n'])
CurrentSolution = ran_permutaive_solution(sol)
SolutionCost = objective_func(sol,tsp)
#--------------------------------------------------
#Initialize Best Solution Ever Found
#--------------------------------------------------
BestSol = sol
#--------------------------------------------------
#Array to hold Best Cost Values
#--------------------------------------------------
#BestCost = num.zeros([MaxIt,1],dtype=int)
#--------------------------------------------------
#Initial Temp.
#--------------------------------------------------
T=T0
#--------------------------------------------------
#SA Main loop
#--------------------------------------------------
#--------------------------------------------------
for it in range(1,MaxIt):
 for subit in range(1,MaxSubIt):

     # --------------------------------------------------
     #Create and Evaluate initial new solution
     # --------------------------------------------------
     newSolution = swap(sol)
     newSolutionCost = objective_func(newSolution,tsp)

     if(newSolutionCost<=SolutionCost):
      BestSol=newSolution
      BestCost = objective_func(BestSol,tsp)
     else:
      Delta = newSolutionCost - SolutionCost
      P = m.exp(-Delta/T)
      if(ran.uniform(0,1)<=P):
       BestSol = newSolution
       BestCost = objective_func(BestSol,tsp)

# Store Best Cost ever Found
#sprint(BestSol)
BestCost = objective_func(BestSol,tsp)

#Update Best Solution ever Found
if(SolutionCost<=BestCost): BestSol = sol;

print("**Best Cost**=>%d"%(BestCost))
#Update Temp.
T = alpha*T



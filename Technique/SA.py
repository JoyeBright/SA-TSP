from MetaHeuristics.Problem.tsp import ran_permutaive_solution,main
from MetaHeuristics.ObjectiveFunction.tsp import objective_func
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
CurrentSolution = sol
SolutionCost = objective_func(sol,tsp)
#--------------------------------------------------
#Initialize Best Solution Ever Found
#--------------------------------------------------
BestSol = CurrentSolution
#--------------------------------------------------
#Array to hold Best Cost Values
#--------------------------------------------------
BestCost = 99999999
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
      #print(CurrentSolution)
      newSolution = swap(CurrentSolution)
      #print(newSolution)
      newSolutionCost = objective_func(newSolution,tsp)
      if(newSolutionCost<=SolutionCost):
       CurrentSolution=newSolution
       BestCost = objective_func(CurrentSolution,tsp)
      else:
       Delta = newSolutionCost - SolutionCost
       P = m.exp(-Delta/T)
       if(ran.uniform(0,1)<=P):
        CurrentSolution = newSolution
        BestCost = objective_func(CurrentSolution,tsp)

     # Update Temp.
     T = alpha * T
     # Store Best Cost ever Found
     BestCost = objective_func(CurrentSolution,tsp)

print("**Best Cost**=>%d"%(BestCost))


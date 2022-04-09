from archer import ArcherProblem
from search import *
import random
import timeit

#---this is the main module where the algorithm is ran---
#---Here there is also implemented the random generator of the input data ---

def main():
   #this is where the random generating of the input data begins
    k=random.randint(4,10) #the size of the grid
    w=random.randint(0,k-1) #this is the range of each archer as stated in the homework(the maximum range is less than the length of the grid)
    restrict=[]  #the restrict list acts as a list which will hold the position of the walls
    bool=True      #this bool variable is used to not have the walls placed on the same position more than once
    
    W=random.randint(0,k-1)  #W will be an integer that is less than the length of the grid and represents the number of walls
    for iterator in range(W):        #here we iterate until we get W restrictions for our walls
        number=random.randint(0,k-1)   
        for check in range(len(restrict)):
           if number==restrict[check]:
               bool=False
        if bool==True:
            restrict.append(number)
    print("The number of walls is:",end="")
    print(len(restrict))
     #this is where the random generating of the input data ends
    placement=[-1]*k #we need to initialize all the elements of the list as -1 first(it means there is nothing placed on the board)
    start = timeit.timeit() #the start timer of the algorithm used to measure the running time
    path = depth_first_tree_search(ArcherProblem(k,w,placement),k,restrict) #the algorithm that runs our problem using DFS
   
    print(path, '\n')
    end = timeit.timeit() #the total running time
    print("The running time of the algorithm is",end=" ")
    print(end - start)

if __name__ == "__main__":
    main()

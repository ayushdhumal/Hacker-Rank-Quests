#!/bin/python3

#The link for this problem is: https://www.hackerrank.com/challenges/staircase/problem

# Complete the staircase function below.
def staircase(n):
    
    #Keeping a track of our count
    Counter = 1
    
    #Iterating through 1 to n using a while loop
    while(Counter <= n):
        
        #Using rjust for padding our staircases
        print(('#' * Counter).rjust(n))
        
        #Increasing the counter by 1
        Counter += 1

if __name__ == '__main__':
    
    #Storing th number of stairs we have to build
    n = int(input())
    
    #Calling the function
    staircase(n)


#!/bin/python3

#The link for this problem can be found at: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    #Setting the minimum score to its initial value
    min_value = scores[0]

    #Initializing a counter and setting it to 0
    min_count = 0

    #Setting the maximum value of the score to 0
    max_value = scores[0]

    #Initializing the counter and setting it to 0
    max_count = 0

    #Using a for loop to iterate through the array and comparint the values
    for x in (scores):

        #If x is smaller than the initial value, replace it and increase teh counter
        if(x<min_value):
            min_value = x
            min_count += 1

        #Elseif x is smaller than the initial value, replace it and increase teh counter
        elif(x>max_value):
            max_value = x
            max_count += 1

        #Returning our counter vcariables
    return (max_count, min_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

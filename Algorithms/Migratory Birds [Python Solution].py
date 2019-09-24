#!/bin/python3

#The link for this problem can be found at: https://www.hackerrank.com/challenges/migratory-birds/problem

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    #Creating an array of 6 0s to store our count of each bird
    birds_freq = 6*[0]
    for x in (arr):
    #Iterating through the loop and incrementing the count by one for every bird
        birds_freq[x] += 1
    #Returning the highest index
    return birds_freq.index(max(birds_freq))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

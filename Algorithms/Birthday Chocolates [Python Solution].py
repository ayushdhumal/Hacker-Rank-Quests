#!/bin/python3

#The link for this problem can be found at: https://www.hackerrank.com/challenges/the-birthday-bar/problem

import math
import os
import random
import re
import sys




def birthday(n, s, d, m):
    #Setting the count value equals to 0
    count = 0
    #Iterating through the array
    for i in range(0,n):
        #Storing the sum of the elements from i to m (the birthday months) in the total variable
        total = sum(s[i:m+i])
        #If the total is equals to the d(birth date), then increment the count by 1
        if total == d:
            count+=1
    #Return the count once the progrm is run
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(n, s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

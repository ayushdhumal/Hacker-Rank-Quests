#!/bin/python3

#The link for this problem can be found at: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#Importing the required libraries
from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.

def divisibleSumPairs(n, k, ar):

    count = 0
    sum_lst = list()
    #Creating all possible combinations of 2 and storing it in a form of list
    combs = (list(combinations(ar, 2)))

    #Suming up those combinations and storing them in an array

    for i in combs:
        sum_lst.append(i[0] + i[1])

    #Going through the summed up list and checking to see if any of them is divisible by k
    for i in sum_lst:
        if (i % k) == 0:
    #If there exists any, increasing the count by one
            count += 1
    #return the count
    return count              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

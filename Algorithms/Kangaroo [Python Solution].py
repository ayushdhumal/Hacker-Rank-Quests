#!/bin/python3
#THe link for this problem can be found at https://www.hackerrank.com/challenges/kangaroo/problem
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
#Going through 10000 iterations
    for n in range(10000):
    #If they are same initially or after the previous iteration return Yes
        if((x1+v1)==(x2+v2)):
            return "YES"
        #Add steps in each iterations
        x1+=v1
        x2+=v2
    #if the loop ends, return No
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import os

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
#Initializing the count variable
    count=0
#Storing the highes number of the array
    big = max(ar)
#Iterating through the array to see any other element of the same size
    for i in range(len(ar)):
#If there exists any, increase the count
        if(ar[i]==big):
            count+=1
#Return the count 
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#Getting the number of the candles
    ar_count = int(input())
#Storing the element in the array
    ar = list(map(int, input().rstrip().split()))
#Calling the function and storing the result
    result = birthdayCakeCandles(ar)
#Printing the result
    fptr.write(str(result) + '\n')

    fptr.close()

#This question can be found on: https://www.hackerrank.com/challenges/diagonal-difference/problem

import os

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    #Variable for storing the sum from Left to Right
    sum_from_left = 0
    #Variable for storing the sum from right to left
    sum_from_right = 0
    #Inititating the for loop in the range of our array length
    for i in range (n):
        #Calculating the Sum
        sum_from_left += arr[i][i]
        x = n-i-1
        sum_from_right += arr[i][x]
    #Storing its absolute value
    AbsoluteValue = abs(sum_from_left-sum_from_right)
    #Returning the absolute value
    return AbsoluteValue    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    #Storing the length of the array
    n = int(input().strip())

    #Declaring an array
    arr = []

    #Storing the input array in the form of a 2-d array
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    #Gwtting the result from the function and storing it in a variable
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

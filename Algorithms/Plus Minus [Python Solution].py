#!/bin/python3
#The link for this challenge is: https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr, n):

    #Storing the Length of the array in a variable. #If we don't get 'n', we can comment out the next line
    #Length = len(arr)

    #Counting the number of zeroes our array contains
    Zeroes = sum(j == 0 for j in arr)

    #Counting the positive numbers our array contains
    Negative = sum(j < 0 for j in arr)

    #Counting the negative numbers our array contains
    Positive = sum(j > 0 for j in arr)

    #Printing the result in the required format
    print(round(Positive/n, 3))
    print(round(Negative/n, 3))
    print(round(Zeroes/n, 3))

if __name__ == '__main__':

    #The number of elements we will be getting in our input 
    n = int(input())

    #Storing the numbers in the arr variable
    arr = list(map(int, input().rstrip().split()))

    #Calling the defined function
    plusMinus(arr, n)

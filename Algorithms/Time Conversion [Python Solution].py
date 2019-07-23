#!/bin/python3
#This puzzle can be found at: https://www.hackerrank.com/challenges/time-conversion/problem


import os

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #This will split the given string through the :
    time = s.split(":")
    #Checking whether the given input is a PM or AM. If it is, adding 12 hours to it
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    #thtime = Time in 24 hour format
    thtime = ':'.join(time)
    #Returning the time in twenty four hour format
    return str(thtime[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    #Getting the imput
    s = input()

    #Storing the results in a variable
    result = timeConversion(s)

    #Displaying the results
    f.write(result + '\n')

    f.close()

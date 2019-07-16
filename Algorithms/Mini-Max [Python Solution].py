#This problem can be found on this link: https://www.hackerrank.com/challenges/mini-max-sum/problem

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #Storing the sum of the array in the integer
    SumOfArray = sum(arr)
    #Evaluating the minimum sum and the maximum sum by subtracting the Max element and the Min element of the array respectively.
    print(SumOfArray - max(arr), SumOfArray - min(arr))

if __name__ == '__main__':

    #Storing the input
    arr = list(map(int, input().rstrip().split()))

    #Calling the function
    miniMaxSum(arr)

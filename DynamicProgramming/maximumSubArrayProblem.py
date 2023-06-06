import sys

def maximumSubArray(arr):
    maximumSum=-sys.maxsize
    for i in range(len(arr)):
        sum=0
        for k in range(i,len(arr)):
            sum=sum+arr[k]
            if sum>maximumSum:
                maximumSum=sum
    return maximumSum


test=maximumSubArray([-2,-1,-3,-4,-1,-2,-5,-4])
print(test)
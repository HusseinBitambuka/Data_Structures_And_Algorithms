import sys
# naive recursive solution
def cutRod(P,n):
    '''This function solve the cutting rod problem using an inefficient recursive solution. it takes in the list of prices per each cut length P
    and the length of the rod n'''
    if n==0: 
        return 0
    q=-sys.maxsize # this is the equivalent of the Java type.MIN_VALUE
    for i in range(n):
        q=max(q,P[i]+cutRod(P,n-(i+1))) #try to cut the rod to get the price P[i] and combine that with the most optimal way to cut the rod of length n-1

    return q


p=[1,5,8,9,10,17,17,20,24,30]
print(len(p))
n=6

print(" the optimal revenue from cutting the rod of length "+str(n)+" is "+str(cutRod(p,n)))

print("")

#The computation time for the above algorithm is crazy!. We recursivelly compute the same value several times.
# Take the example of n=6. we compute the value of cutRod(p,1) for every i. Dynamic Programming solve this problem by storing the computed value in an array

def helper(p,n,r):
    if r[n-1]>=0:
        return r[n-1]
    if n==0:
        q=0
    else:
        q=-sys.maxsize
        
        for i in range(n):
            q=max(q,p[i]+helper(p,n-(i+1),r)) #try to cut the rod to get the price P[i] and combine that with the most optimal way to cut the rod of length n-1

    r[n-1]=q
    return q
     

def memoizedCutRod(p,n):
    r=[]
    for i in range(n):
        r.append(-sys.maxsize) # fill up the array with -infinity
    return helper(p,n,r)

print(" the optimal revenue from cutting the rod of length "+str(n)+" is "+str(memoizedCutRod(p,n)))


# Buttom up approach
 
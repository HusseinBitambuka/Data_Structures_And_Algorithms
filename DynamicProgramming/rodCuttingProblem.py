import sys
# naive recursive solution
def cutRod(P,n):
    '''This function solve the cutting rod problem using an inefficient recursive solution. it takes in the list of prices per each cut length P
    and the length of the rod n'''
    if n==0: # 
        return 0
    q=-sys.maxsize # this is the equivalent of the Java type.MIN_VALUE
    for i in range(n):
        q=max(q,P[i]+cutRod(P,n-1)) #
    return q


p=[1,5,8,9,10,17,17,20,24,30]
print(len(p))
n=3

print(" the optimal revenue from cutting the rod of length "+str(n)+" is "+str(cutRod(p,n-1)))

string="midos"
print(string[-1])
mido=[]

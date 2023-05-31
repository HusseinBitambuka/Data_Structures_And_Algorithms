def insertion_sort(A)->list:
    '''This function takes an array of data and returns a sorted version of that array using the insertion sort Algorithms
    '''
    for j in range(1, len(A)): 
        key=A[j] # take an alement as the starting key that you are going to compare with the rest of the data in the array. in thi case we are starting with the second element in the list
        i=j-1 # the element that precedes the key
        while i>=0 and A[i]>key: # check to see if all the elements on the left hand of the key are less than the key. Otherwise, move that element to the righ hand of the key
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key # take the element that comes after the current key as the new key

# Buble Sort

def buble_sort(A)->list:
    '''The buble sort algorithm sorts an array of data by checking if the nth element is smaller than n-1th element and swap their position.
    the idea here is make sure that the element on the right side of the key are all greater than the key.
    by reapiting this process for all the n elements in an array, we end up with a sorted array'''
    for i in range(len(A)-1): 
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j] # swap the nth element with the n-1th element
    
# Merge sort

'''Merge sort algorithm follows the divide and conquer approach. It has the divide, conquer, and combine approach
'''


def merge(A,p,q,r):
    '''This is the conquer part of the merge sort.
    '''
    leftLenght=q-p 
    rightLenght=r-q
    left=[]
    right=[]
    for i in range(leftLenght): # fill up the element in the left array
        left.append(A[i])
    for j in range(rightLenght): # fill up the elemet of the right array
        right.append(A[j])

    # 
    i,j=0
    k=p
    while(i<leftLenght and j<rightLenght): # if either of the array is empty, terminate the loop
        if(left[i]<right[i]): # check to see which between the left and the right element goes first in the array
            A[k]=left[i]
            i=i+1
        else:
            A[k]=right[j]
            j=j+1
        k=k+1
# this step fill up whatever elements are left in the array
    while(i<leftLenght):
        A[k]=left[i]
        i=i+1
        k=k+1
    while(j<rightLenght):
        A[k]=right[i]
        j=j+1
        k=k+1


def merge_sort(A,p,r):
    '''This is the devide and combine part of the merge sort algoritm'''
    if p<r:
        q=[(p+r)/2]
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        
def mergeSort(A):
    "this is a helper method for the user"
    p=len(A)
    r=0
    merge_sort(A,p,r)


#Examples
StringEXample=["Mtu Mwema","New York","California","Bujumburan","Asiatique","Gishingano","Nyakazu"]

print("Before sorting \n")
print("---------------------------------")
print(StringEXample)

insertion_sort(StringEXample)

print("\n After sorting with insertion sort \n")
print("---------------------------------")
print(StringEXample)

StringEXample1=["Mtu Mwema","New York","California","Bujumburan","Asiatique","Gishingano","Nyakazu"]

print("Before sorting \n")
print("---------------------------------")
print(StringEXample1)

buble_sort(StringEXample1)

print("\n After sorting with buble sort \n")
print("---------------------------------")
print(StringEXample1)

StringEXample2=["Mtu Mwema","New York","California","Bujumburan","Asiatique","Gishingano","Nyakazu"]

print("Before sorting \n")
print("---------------------------------")
print(StringEXample2)

mergeSort(StringEXample2)

print("\n After sorting with merge sort \n")
print("---------------------------------")
print(StringEXample2)
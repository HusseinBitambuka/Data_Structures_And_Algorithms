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

def buble_sort(A)->list:
    for i in range(len(A)-1):
        
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]

    

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
def find(T,P):
    '''Return the lowest index of T at which substring P begins (or else -1).'''
    longerString,subString = len(T),len(P) 
    for i in range(longerString-subString+1): # just check in the range where the substring can be found
        k = 0                                   # k is the number of characters matched so far
        while k < subString and T[i+k] == P[k]:   # check if the index of the larger string maches the index of the smaller string and keep comparing these 
            k += 1
        if k == subString:  # if k is equal to the length of the substring then we have found the substring in the larger string
            return i
    return -1


longerString="watu wenye akili wanaelewa"
subString="wenye"
print(find(longerString,subString))

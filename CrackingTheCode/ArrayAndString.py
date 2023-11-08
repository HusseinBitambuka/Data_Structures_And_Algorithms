# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# 1.1
def isUnique(string):
    dict = {} # empty dictionary
    for char in string: # iterate through string
        if char in dict:
            return False
        else:
            dict[char] = 1
    return True


test = "hello"
print(isUnique(test))
#1.2
# Given two strings, write a method to decide if one is a permutation of the other.

def isPermutation(string1, string2):
    setChecker = set() # empty set
    for char in string1:
        setChecker.add(char) # add all characters of either of the strings into the set
    if len(string1) != len(string2): # check if the length of the strings are equal, and if not, return False
        return False
    for char in string2: # check if each character of the remaining string is in the set
        if char not in setChecker:
            return False
    return True


test1 = "hello"
test2 = "olhle"
print(isPermutation(test1, test2))

#1.9
# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2,
# write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation
# of "erbottlewat").

def isSubstring(string1, string2):
    if len(string1) != len(string2): # again check if the strings have the same number of characters
        return False
    for i in range(len(string1)): # check the first character of the second string in the first string
        if string1[i] == string2[0]:
            if string1[i:] + string1[:i] == string2: # if the first character is found, check if the rest of the string is the same
                return True
    return False

# computing factorial with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# reverse a string with recursion
def reverse(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse(string[:-1]) 
    
print(reverse("hello"))

# palindrome checker with recursion
def isPalindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return isPalindrome(string[1:-1])
        else:
            return False

print(isPalindrome("racecar"))

# Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.
def minMax(sequence):
    if len(sequence) == 1:
        return sequence[0], sequence[0]
    else:
        min, max = minMax(sequence[1:])
        if sequence[0] < min:
            min = sequence[0]
        if sequence[0] > max:
            max = sequence[0]
        return min, max
    

print(minMax([1,2,3,4,5,6,7,8,9,10]))

print(4%2)
def reversingString(s):
    if len(s) == 1:
        return s
    return s[-1] + reversingString(s[:-1])
print(reversingString("watu wenye akili wanaelewa"))

array = [1,2,3,4,5,6,7,8,9,10]
if array[len(array)]:
    print("yes")
else:
    print(array[len(array)-1])
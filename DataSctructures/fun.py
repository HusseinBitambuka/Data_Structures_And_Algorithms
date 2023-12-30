def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    answer = []

    def fill(arr, tracker, numRows, answer):
        answer.append(arr[:])
        if tracker >= numRows:
            return

        new = []
        new.append(1)
        element = 0
        for i in range(1, len(arr)):
            element = arr[i]
            next_element = element + arr[i - 1]
            new.append(next_element)
        new.append(1)
        fill(new, tracker + 1, numRows, answer)

    fill([1], 1, numRows, answer)
    return answer

# Example usage:
numRows = 5
result = generate(numRows)
print(result)

def magicArray(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + magicArray(arr[1:])

print('\n') 

print(magicArray([1,2,3,4,5,6,7,8,9,10]))
    
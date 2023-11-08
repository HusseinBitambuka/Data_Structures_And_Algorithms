class Stack:
    class Node():
        # internal Node
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        # initialize the stack with an empty head node and a counter of 0
        self.head = None
        self.tail = None
        self.length = 0
    def push(self, element):
        # push an element to the top of the stack
        newNode = self.Node(element)
        newNode.next = self.head
        self.head = newNode
        # set the pointer to the the first element to be the tail
        if self.length == 0:
            self.tail = newNode
        self.length += 1

    def pop(self):
        # pop an element from the top of the stack
        if self.length == 0:
            return None
        valueToreturn = self.head.value
        self.head = self.head.next
        self.length -= 1 # decrement the lenght of 
        if self.length == 0:
            self.tail = None
        return valueToreturn
    def popNode(self):
        if self.length == 0:
            return None
        nodeToReturn = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return nodeToReturn
    def peek(self):
        # return the top element of the stack
        if self.length == 0:
            return None
        return self.head.value
    def printStack(self):
        # print the stack
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

myTest = Stack()
myTest.push(1)
myTest.push(20)
myTest.push(45)
myTest.printStack()
print(myTest.peek())
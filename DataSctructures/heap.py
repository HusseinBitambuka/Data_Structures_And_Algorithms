import math
class MaxHeap():
    def __init__(self):
        self.capacity = 100
        self.heap = [None] * self.capacity # list to store the heap
        self.size = 0 # size of the heap

    def insert(self, val):
        if self.size == self.capacity:
            self.double_capacity()
        self.heap[self.size] = val
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)
        

    def extract_max(self):
        max = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down(0)
        return max

    def heapify_down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if self.size > left and self.heap[largest] < self.heap[left]:
            largest = left
        if self.size > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)

    def print_heap(self):
        if self.size == 0:
            print("Empty Heap")
        else:
            print(self.heap[:self.size])
    def double_capacity(self):
        self.capacity *= 2
        new_heap = [None] * self.capacity
        for i in range(self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
heap.insert(20)
heap.insert(200)

print(heap.extract_max())

heap.print_heap()


# fun with Min Heap leetcode 973

class Minheap():
    def __init__(self, capacity):
        self.heap = [None]*capacity
        self.size = 0

    def heapifyUp(self, index):
        '''maintains the heap property by swapping the parent with the child if the parent is greater than the child'''
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[parent][0] > self.heap[index][0]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapifyUp(parent)
    def heapifyDown(self, index):
        '''maintains the heap property by swapping the parent with the child if the parent is greater than the child'''
        left = (index * 2) + 1 # left child
        right = (index * 2 ) + 2 # right child
        smallest = index # parent
        
        if self.size > left and self.heap[smallest][0] > self.heap[left][0]: # if the left child is smaller than the parent, set the smallest to the left child
            smallest = left
        if self.size > right and self.heap[smallest][0] > self.heap[right][0]: # if the right child is smaller than the parent, set the smallest to the right child
            smallest = right
        if smallest != index: # if the parent is not the smallest, swap the parent with the smallest child
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapifyDown(smallest)
    def getDistance(self, p):
        return math.sqrt(p[0]**2 + p[1]**2) # returns the distance of the point from the origin

    def insert(self, p):
        '''inserts a point into the heap'''
        d = self.getDistance(p) # get the distance of the point from the origin
        element =  [d, p] # create a list with the distance and the point
        self.heap[self.size] = element
        self.heapifyUp(self.size) # maintain the heap property
        self.size += 1

    def getMin(self):
        '''returns the minimum element in the heap'''
        minEl = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heapifyDown(0)
        self.size -= 1
        return minEl

    def returnKC(self, k):
        '''returns the k closest points to the origin'''
        arr = [None]*k
        i = 0
        while k > 0:
            arr[i] = self.getMin()[1] # get the point from the minimum element
            i += 1
            k -= 1
        return arr

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minH = Minheap(len(points))
        for p in points:
            minH.insert(p)
        return minH.returnKC(k)



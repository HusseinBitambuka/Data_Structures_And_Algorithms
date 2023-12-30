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


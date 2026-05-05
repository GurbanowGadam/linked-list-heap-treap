class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def search(self, value):
        return value in self.heap

    def delete(self, value):
        if value not in self.heap:
            return False

        index = self.heap.index(value)
        self.heap[index] = self.heap[-1]
        self.heap.pop()

        if index < len(self.heap):
            parent = (index - 1) // 2

            if index > 0 and self.heap[index] < self.heap[parent]:
                self.heapify_up(index)
            else:
                self.heapify_down(index)

        return True

    def display(self):
        print(self.heap)

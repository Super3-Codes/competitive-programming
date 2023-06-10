class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = self.heapSort(stones,len(stones))
        while len(heap) > 1:
            print(heap)
            first, second = heap.pop() , heap.pop()
            if first != second:
                result = abs(first-second)
                heap.append(result)
                self.heapSort(heap,len(heap))
        if len(heap) == 1:
           return heap[0]
        return 0 
        
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def heapSort(self, arr, n):
        self.buildHeap(arr, n)# n * h

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr

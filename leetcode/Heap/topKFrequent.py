class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        hashMap = {}
        for index , word in enumerate(words): 
            hashMap[word] = hashMap.get(word,0) + 1

        for key, value in hashMap.items():
            heap.append((-value,key))
        heapq.heapify(heap)

        result = (heapq.heappop(heap)[1] for _ in range(k))

        return result

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0]*1000
        
        for num, a, b in trips:
            for i in range (a, b):
                path[i] += num
                if path[i] > capacity: return False
                
        return True

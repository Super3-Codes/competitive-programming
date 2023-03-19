class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = max(piles)
        while right >= left:
            mid = (right + left)//2
            
            eating_speed = 0

            for pile in piles:
                eating_speed += math.ceil(pile/mid)
            if eating_speed <= h:
               result = min(result,mid)
               right = mid -1
            else:
                left = mid + 1
        return result
            

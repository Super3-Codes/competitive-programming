class Solution:
    def checker(self,weights,validDay,mid):
        value = 0
        daysNeeded = 1
        for weight in weights:
            if value + weight > mid:
                daysNeeded += 1
                value = weight
            else:
                value += weight
        return daysNeeded
         
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = float('inf')
        while left <= right:
            mid = (left + right) // 2
            daysNeeded = self.checker(weights, days, mid)
            if daysNeeded <= days:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

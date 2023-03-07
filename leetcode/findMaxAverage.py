  def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        result = sum(nums[:k])/k
        sumValue = sum(nums[:k])

        while right < len(nums):
            sumValue = (sumValue - nums[left]) + nums[right]
            result = max(result, sumValue/k)
            left = left + 1
            right += 1
        return result

 def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums = set(nums)
        for num in range(length+1):

            if num not in nums:
                return num

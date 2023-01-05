def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for x in range(len(nums)):
            for y in range(x+1, (len(nums))):
                if nums[x] == nums[y]:
                    count += 1
        return count

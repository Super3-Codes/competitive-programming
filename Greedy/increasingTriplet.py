class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = nums[0]
        j = inf 
        for x in nums:
            if x < i:
                i = x
            elif i < x and x < j:
                j = x
            elif i < x and x > j:
                return True

        return False


               




        

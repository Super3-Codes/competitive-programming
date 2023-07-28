class Solution:

    def rob(self, nums: List[int]) -> int:
        rob, notrob = 0, 0
        for num in nums:
            rob, notrob = notrob + num , max(rob,notrob)
        return max(notrob,rob)
            
         


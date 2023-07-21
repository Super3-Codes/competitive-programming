class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0     
        nums.sort()
        n = len(nums)-1
        
        values = [(2,n-1),(1,n-2),(3,n),(0,n-3)]
        result = inf

        for i in range(4):
            start , end = values[i]
            result = min(result,abs(nums[start]-nums[end]))
        return result
  
   
    
     

        

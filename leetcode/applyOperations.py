  def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        while(right < len(nums)):
            if nums[right] == nums[left]:
                nums[left] = nums[left] * 2
                nums[right] = 0
            right += 1
            left += 1
        right = 0
        left = 0 
        for i , num in enumerate(nums):
            if num == 0:
                right = i
                left = i + 1
                while(left > right and left < len(nums)):
                    if(nums[left]  != 0):
                        nums[left] , nums[right] = nums[right], nums[left]
                        break;
                    else:
                        left += 1
        return nums

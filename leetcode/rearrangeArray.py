def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)-1):

            if nums[i-1] < nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

            elif nums[i+1] < nums[i] < nums[i-1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        

        return nums

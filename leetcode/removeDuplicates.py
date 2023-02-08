    def removeDuplicates(self, nums: List[int]) -> int:

        left = 1
        right = 1
        index = len(nums)-1

        while(left < len(nums)):
            if nums[left] != nums[left-1]:
                nums[right] = nums[left]
                right += 1
            left += 1
        print(right)

        while(index >= right):
            nums.pop()
            index -= 1
            
       
        return left

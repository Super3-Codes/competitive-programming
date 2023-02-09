    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums , left , right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        k = k % len(nums)
        left, right = 0 , len(nums)-1
        reverse(nums,left,right)

        left , right = 0 , k - 1
        reverse(nums,left,right)

        left, right = k, len(nums)-1
        reverse(nums,left,right)

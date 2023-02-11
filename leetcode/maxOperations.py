    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        
        while(right > left):
            result = nums[right] + nums[left]
            if (result == k):
                count += 1
                left += 1
                right -= 1
            elif(result > k):
                right -= 1
            else:
                left += 1
        return count

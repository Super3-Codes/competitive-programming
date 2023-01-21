class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = 0
        nums = []
        index = 0
        for i in range(1, n+1):
            nums.append(i)
        size = len(nums)
        while(size > 1):
            if(index == n ):
                index = 0
            if(nums[index] != 0):
                count += 1
            if count == k :
                nums[index] = 0
                size -= 1
                count = 0
            index += 1
        for num in nums:
            if(num != 0):
                return num

                

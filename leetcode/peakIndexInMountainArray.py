class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #find the mid variable
        #check if the number to the right it is less than the mid
        #check if the number to the left is also less than the mid
        left, right = 0, len(arr) - 1
    
        while left < right:
            mid = (left + right) // 2
        
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
            
        return left

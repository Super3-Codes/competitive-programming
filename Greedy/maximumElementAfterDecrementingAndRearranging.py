class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for index, value in enumerate(arr[1:], 1):
            if 1 < (value - arr[index-1]):
                arr[index] = arr[index-1] + 1
        return arr[-1]

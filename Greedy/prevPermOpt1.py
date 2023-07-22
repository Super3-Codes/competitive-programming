class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        first , last = len(arr)-2, len(arr)-1
        while first >= 0:
            if arr[first] > arr[last]:
                break
            else:
                first -= 1
                last -= 1
        if first < 0:
            return arr
        key = last
        while last < len(arr):
            if arr[last] < arr[first] and arr[last] > arr[key]:
                key = last
            last += 1
        arr[first], arr[key] = arr[key], arr[first]
        return arr

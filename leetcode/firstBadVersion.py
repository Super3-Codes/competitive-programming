class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 1
        lastBadVersion = 0

        while right >= left:
            mid = (right + left)//2

            if isBadVersion(mid):
                lastBadVersion = mid
                right = mid -1
            else:
                left = mid + 1
        return lastBadVersion

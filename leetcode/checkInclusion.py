class Solution:
    def checkInclusion(self,s1: str, s2: str) -> bool:
        lookup = [0] * 26
        lookup2 = [0] * 26
        right = 0
        left = 0
        for i in range(len(s1)):
            lookup[ord(s1[i]) - ord('a')]+= 1
        if lookup == lookup2:
            return True
        while right < len(s2):
            lookup2[ord(s2[right]) - ord('a')]+= 1
            if lookup == lookup2:
                return True
            while right - left + 1 >= len(s1):
                lookup2[ord(s2[left]) - ord('a')]-= 1
                left+= 1
            right+= 1
        return False

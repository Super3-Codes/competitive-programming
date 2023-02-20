def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        map = {}
        left = 0
        right = 0
        count = 0
    
        while right < len(s):
            while s[right] in map:
                del map[s[left]]
                left += 1
            map[s[right]] = right
            count = max(count, abs(right - left + 1))
            right += 1
        return count

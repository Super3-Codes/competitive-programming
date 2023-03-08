class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left = 0
        right = 0
        max_count = 0
        result = 0
        char_count = defaultdict(int)

        while right < len(s):
            window_size = right - left + 1
            if s[right] in char_count:
                char_count[s[right]] += 1
                max_count = max(char_count.values())
            else:
                char_count[s[right]] = 1
                max_count = max(char_count.values())

            while window_size - max_count > k and left <= right:
                char_count[s[left]] -= 1
                max_count = max(char_count.values())
                left += 1
                window_size = right - left + 1

            result = max(result, right - left + 1)
            right += 1

        return result

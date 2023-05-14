class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(position, used):
            if position > n:
                return 1

            count = 0
            for i in range(1, n + 1):
                if not used[i] and (i % position == 0 or position % i == 0):
                    used[i] = True
                    count += backtrack(position + 1, used)
                    used[i] = False

            return count

        used = [False] * (n + 1)
        return backtrack(1, used)

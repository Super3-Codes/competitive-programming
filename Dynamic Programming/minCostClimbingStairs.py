from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dp(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]

            firstStep = dp(index + 1)
            secondStep = dp(index + 2)
            result = min(firstStep, secondStep) + cost[index]
            memo[index] = result
            return result

        return min(dp(0), dp(1))

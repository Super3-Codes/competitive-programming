class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x^y
        result = 0
        while diff:
            result+= diff&1
            diff>>=1
        return result

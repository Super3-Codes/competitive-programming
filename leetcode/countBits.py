class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            value = bin(i).split("b")
            result = value[1].count("1")
            output.append(result)
        return output

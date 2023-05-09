class Solution:
    def findComplement(self, num: int) -> int:
        result = bin(num).split("b")
        value = result[1]
        print(value)
        stack = []
       
        for v in value:
            if v == "0":
                stack.append("1")
            else:
                stack.append("0")
        output = "".join(stack)
        result[1] = output
        value = "".join(result)
        return int(value,2)

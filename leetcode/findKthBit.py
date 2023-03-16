class Solution:
    def invert(self, s):
        value = ""
        for i , c in enumerate(s):
            if c == "0":
                value = value +  "1"
            else:
                value = value + "0"
        return value
   
    def findKthBit(self, n: int, k: int) -> str:
        
        def compute(n,k):
            if n == 1:
                return "0"
            result = compute(n-1,k)
            value = self.invert(result.strip())
            constructedValue = result + "1" + value[::-1]
            return constructedValue
        output = compute(n,k)
        print(len(output))
        return output[k-1]

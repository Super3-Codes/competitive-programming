class Solution:
    def splitString(self, s: str) -> bool:
        self.res = False
        def helper(s, k):
            n1 = int(s[:k+1])
            for j in range(k+1, len(s)):
                n2 = int(s[k+1:j+1])
                if n1 - n2 == 1:
                    if j == len(s)-1:
                        self.res = True 
                    else: 
                        helper(s[k+1:], j-(k+1))
                if n2 >= n1:
                    break
                        
        for i in range(len(s)):
            helper(s, i)
        return self.res

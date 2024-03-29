   def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1

        def reverse(s,left,right):
            if left > right:
                return
            s[left],s[right] = s[right],s[left]
            reverse(s,left+1,right-1)
        reverse(s,left,right)

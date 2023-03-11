  def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == ')' and stack and stack[-1] == c:
                stack.pop()
                stack.append(1)
            elif c == ')' and stack and stack[-1] != c:
                result = 0
                while stack and stack[-1] != c:
                    result += stack.pop()
                stack.pop()
                stack.append(2*result)
        while stack:
            score += stack.pop()
                
        return score

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for str in tokens:
            if str == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif str == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif str == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif str == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                stack.append(int(str))
        return stack.pop()

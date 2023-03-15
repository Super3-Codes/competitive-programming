 def myPow(self, x: float, n: int) -> float:
        
        def getValue(x,n):
            if n == 0:
                return 1
            if n == 1 or n == -1:
                return x
            elif n % 2 == 0:
                y = getValue(x,n/2)
                y = y * y
            elif n % 2 != 0:
                if n > 0:
                    n = n - 1
                else:
                    n = n + 1
                y = getValue(x,n/2)
                y = (y * y) * x

            return y
        value = getValue(x,n)
        if n < 0:
            value = 1/value
        return value

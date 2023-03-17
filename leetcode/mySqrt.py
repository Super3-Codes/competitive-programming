    def mySqrt(self, x: int) -> int:
        '''
            y * y = x
            y => [1, x]
        '''


        left, right = 0, x
        r = 0
        
        while left <= right:
            mid = (left + right)//2
            sq = mid ** 2
            
            if sq == x or (sq < x and (mid + 1) * (mid + 1) > x):
                return mid

            if  sq > x:
                right = mid - 1
            elif sq < x:
                left = mid +1
            

            else:
                
                return mid
        return r

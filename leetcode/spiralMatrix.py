def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0 , len(matrix[0])
        top, bottom = 0 , len(matrix)
        
        while left < right and top < bottom:
            # go from left to right adding the top elements
            # then move the top down by 1
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            # get the items at the right most colomun 
            for i in range(top,bottom):#1 , 3
                result.append(matrix[i][right-1])
            right -= 1
            #safe a guard if we only have one col or one row matrix
            if not (left < right and top < bottom):
                break
                
            #get the items at the bottom from right to left
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            #get the items in the left most col

            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left += 1
        return result

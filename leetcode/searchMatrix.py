def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        isValid = False
        def binarySearch(nums, targets, right , left):
            while(right >= left):
                middle = left + ((right-left)//2)
                if(nums[middle] == targets ):
                    return True
                elif(nums[middle] > targets):
                    right = middle - 1
                else:
                    left = middle + 1
            return False

        for i in range(len(matrix)):
            isValid = binarySearch(matrix[i] , target , len(matrix[i])-1 , 0 )
            if(isValid):
                break
        return isValid

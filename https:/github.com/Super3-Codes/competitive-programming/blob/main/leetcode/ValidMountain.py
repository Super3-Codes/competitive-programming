def validMountainArray(self, arr: List[int]) -> bool:
        #Find the largest number and there index position 
        #check if the numbers to the right are strictly decreasing 
        #check if the numbers to the left are strictly increasing
        max = -inf
        min = inf
        max_index = 0
        min_index = len(arr) - 1
       

        right = len(arr) - 1
        
        if(sorted(arr) == arr):
            return False
        if(sorted(arr ,reverse = True) == arr):
            return False

        for i , num in enumerate(arr):
            if(num >= max):
                max = num
                max_index = i

        if (max_index == len(arr)-1 or max_index == 0):
            return False
        
        for i in range(max_index-1):
            if arr[i] >= arr[i+1] :
                return False
        for i in range(max_index,len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
            
        return True

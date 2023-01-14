def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i
        for i in range(len(operations)):
            key = operations[i][0]
            value  = operations[i][1]
            result = numbers.get(key)
            if(result != None):
                numbers[value] = result
                numbers.pop(key)
        for key , value in numbers.items():
            nums[value] = key
        return nums  

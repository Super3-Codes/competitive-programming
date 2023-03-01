def countDistinctIntegers(self, nums: List[int]) -> int:
        numbers = set(nums)
        newNumbers = set()
        for num in numbers:
            y = str(num)[-1::-1]
            newNumbers.add(int(y))
        numbers = numbers.union(newNumbers)
        return len(numbers)

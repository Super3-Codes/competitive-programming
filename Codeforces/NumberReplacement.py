N = int(input())
for _ in range((N)):

	n = int(input())

	nums = list(map(int,input().split()))
	
	finalString = input()

	arr = []

	for letter in finalString:
		arr.append(letter)

	result = [""] * n

	for i, char in enumerate(arr):
		for j, num in enumerate(nums):
			number = nums[i]
			if number == num:
				result[j] = char
	output = "".join(result)

	if output != finalString:
		print("NO")
	else:
		print("YES")

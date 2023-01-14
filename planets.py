from collections import Counter
N = int(input())
 
for _ in range(N):
	
	length , cost = (input().split())
	length = int(length)
	cost = int(cost)
	result = 0
 
	nums = list(map(int,input().split()))
 
	count = Counter(nums)
 
	for key , value in count.items():
		result += min(cost,value)
 
 
	print(result)

N = int(input())
 
x = y = z = 0
 
for _ in range(N):
	i , j , k = map(int,input().split())
	
	x = x + i 
	y = y + j
	z = z + k
 
if x == 0 and y == 0 and z == 0:
	print("YES")
else:
	print("NO") 

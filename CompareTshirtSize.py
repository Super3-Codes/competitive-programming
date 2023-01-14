
N = int(input())
for _ in range(N):
 
	sizeA,sizeB = input().split()
 
	a = sizeA[len(sizeA)-1]
	b = sizeB[len(sizeB)-1]
 
	if a != b :
		if(a == 'L' and b != 'L'):
			print(">")
		elif(a == 'M' and b != 'L'):
			print(">")
		else:
			print("<")
	elif a == b :
		if(len(sizeA) == len(sizeB)):
			print("=")
		elif(len(sizeA) > len(sizeB) and a == 'S'):
			print("<")
		elif(len(sizeA) < len(sizeB) and b == 'S'):
			print(">")
		elif(len(sizeA) > len(sizeB) and a == 'L'):
			print(">")
		elif(len(sizeA) < len(sizeB) and b == 'L'):
			print("<")
		

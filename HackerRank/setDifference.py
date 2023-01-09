num1, set_sub1 = int(input()), set(map(int, input().split()))
num2, set_sub2 = int(input()), set(map(int, input().split()))
print(len(set_sub1.difference(set_sub2)))

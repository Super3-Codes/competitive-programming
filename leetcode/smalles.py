t = int(input())
 
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    a.sort()
    isValid = True
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            isValid = False
            break
 
    if isValid:
        print("YES")
    else:
        print("NO")

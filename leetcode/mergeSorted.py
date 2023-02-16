n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0  
j = 0   
merged = []  

while i < n and j < m:
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1


while i < n:
    merged.append(a[i])
    i += 1

while j < m:
    merged.append(b[j])
    j += 1

print(*merged)

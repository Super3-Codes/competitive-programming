n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0  # pointer for array a
j = 0  # pointer for array b
count = 0  # to store the number of elements less than the current element in b
result = []
while j < m:
    while i < n and a[i] < b[j]:
        count += 1
        i += 1
    result.append(count)
    j += 1
print(*result)

N = int(input())
values = {}
count = 0
for _ in range(N):
    word = input()
    if word in values.keys():
        values[word] = values.get(word)+1
    else:
        values[word] = 1
        count = count + 1

print(count)
for word in values:
    print(values.get(word),end=" ")

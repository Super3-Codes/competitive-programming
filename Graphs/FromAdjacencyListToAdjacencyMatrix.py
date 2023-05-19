n = int(input())

adj_list = []
for _ in range(n):
    row = list(map(int, input().split()[1:]))
    adj_list.append(row)

adj_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in adj_list[i]:
        adj_matrix[i][j - 1] = 1

for row in adj_matrix:
    print(*row)

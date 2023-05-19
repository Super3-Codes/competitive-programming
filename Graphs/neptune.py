n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

road_count = 0
for row in matrix:
    road_count += sum(row)

print(road_count// 2)

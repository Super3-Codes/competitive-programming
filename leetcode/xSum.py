N = int(input())
 
 
for _ in range(N):
    n , m = map(int,input().split())
 
    grid = []
 
    for i in range(n):
        grid.append(list(map(int,input().split())))
 
    diagonal = {}
    antiDiagonal = {}
    ans = 0
 
    for i in range(n):
        for j in range(m):
            diagonal[i-j] = grid[i][j] + diagonal.get(i-j,0)
            antiDiagonal[i+j] = grid[i][j] + antiDiagonal.get(i+j,0)
    for i in range(n):
        for j in range(m):
            ans = max(ans, diagonal[i-j] + antiDiagonal[i+j] - grid[i][j])
 
    print(ans)
 

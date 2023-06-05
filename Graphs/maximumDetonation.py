class Solution:
    def maximumDetonation(self, bombs):
        adj_list = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                distance = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                if distance <= r1:
                    adj_list[i].append(j)
                if distance <= r2:
                    adj_list[j].append(i)
                
        def dfs(bomb, visited):
            if bomb in visited:
                return 0
            visited.add(bomb)
            result = 1
            for neighbor in adj_list[bomb]:
                result += dfs(neighbor, visited)
            return result

        maxBombs = 0
        for i in range(len(bombs)):
            result = dfs(i, set())
            maxBombs = max(maxBombs, result)

        return maxBombs

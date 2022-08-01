class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num, m, n = 0, len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # BFS
        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        q.appendleft((nr, nc))
                        grid[nr][nc] = '#'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_num += 1
                    bfs(i, j)
        return island_num


"""      
        def traverse(i, j):
            grid[i][j] = "#"
            for direction in directions:
                row, col = i + direction[0], j + direction[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                    traverse(row, col)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    traverse(r, c)
                    island_num += 1

        return island_num
"""

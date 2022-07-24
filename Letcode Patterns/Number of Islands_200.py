class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

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

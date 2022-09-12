class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, step = 0, 0

        def findI(i, j):
            nonlocal ans, step
            grid[i][j] = 0
            step += 1
            ans = max(ans, step)
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for r, c in directions:
                if 0 <= i + r < len(grid) and 0 <= j + c < len(grid[0]):
                    if grid[i + r][j + c] == 1:
                        findI(i + r, j + c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    findI(i, j)
                    step = 0

        return ans

        # def findI(i, j):
        #     if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
        #         grid[i][j] = 0
        #         return 1 + findI(i - 1, j) + findI(i + 1, j) + findI(i, j + 1) + findI(i, j - 1)
        #     return 0
        # 
        # ans = [findI(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]]
        #
        # return max(ans) if ans else 0

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = 0
        neighbors = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1
                    if i + 1 < m and grid[i + 1][j] == 1:
                        neighbors += 1
                    if j + 1 < n and grid[i][j + 1] == 1:
                        neighbors += 1

        return islands * 4 - neighbors * 2

#         visited = set()

#         def pers(r, c):
#             visited.add((r, c))
#             summ = 0
#             for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#                 if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]):
#                     if grid[r + i][c + j] == 1 and (r + i, c + j) not in visited:
#                         summ += pers(r + i, c + j)
#                     else:
#                         summ += 1
#             return summ

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     return pers(i ,j) - 1


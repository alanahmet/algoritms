class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        p_visited, a_visited = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def traverse(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for direction in directions:
                i, j = r + direction[0], c + direction[1]
                if 0 <= i < rows and 0 <= j < cols:
                    if matrix[i][j] >= matrix[r][c]:
                        traverse(i, j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)
        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val, visited = image[sr][sc], set()

        def fill(r, c):
            image[r][c] = color
            visited.add((r, c))

            for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= r + i < len(image) and 0 <= c + j < len(image[0]):
                    if image[r + i][c + j] == val and (r + i, c + j) not in visited:
                        fill(r + i, c + j)

        fill(sr, sc)
        return image

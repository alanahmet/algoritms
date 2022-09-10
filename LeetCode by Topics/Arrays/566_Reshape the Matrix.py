class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if mat == [] or r * c != len(mat) * len(mat[0]):
            return mat

        res = [[-1] * c for _ in range(r)]
        index = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[index // c][index % c] = mat[i][j]
                index += 1
        return res

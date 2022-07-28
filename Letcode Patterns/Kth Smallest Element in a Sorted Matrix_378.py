class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        indexs = {i: 0 for i in range(len(matrix))}
        smallest = matrix[0][0]
        sorted_arr = []
        new_s = False
        smallest_index = 0
        while indexs:
            for i, v in indexs.items():
                if new_s == True:
                    smallest_index = i
                    new_s = False
                if matrix[i][v] <= smallest:
                    smallest_index = i
            smallest = matrix[smallest_index][indexs[smallest_index]]
            print(smallest_index, indexs, smallest)
            indexs[smallest_index] += 1
            sorted_arr.append(smallest)
            if indexs[smallest_index] == len(matrix):
                indexs.pop(smallest_index)
                new_s = True
        print(sorted_arr)
        return sorted_arr[k - 1]


print(Solution().kthSmallest([[1,4],[2,5]], 2))

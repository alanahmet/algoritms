class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        preMap = {a: [] for a in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        res = []
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                res.append(crs)
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        print(res)
        return True


print(Solution().canFinish(3, [[1, 0], [2, 0], [3, 1], [3, 2]]))

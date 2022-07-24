class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        preMap = {a: [] for a in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        res = []
        visited = set()
        cyc = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cyc:
                return False

            cyc.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.add(crs)
            cyc.remove(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return res

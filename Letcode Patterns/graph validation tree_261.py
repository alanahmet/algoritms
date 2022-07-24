class Solution:
    def validTree(self, n, edges):
        if not n: return True

        adj = {i: [] for i in range(n)}
        for n, v in edges:
            adj[n].append(v)
            adj[v].append(n)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
                return True

        return dfs(0, -1) and len(visited) == n

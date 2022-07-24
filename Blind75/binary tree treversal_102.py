import collections


class Solution:
    def levelOrder(self, root: []) -> [[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


""" My dummy version
        res = []
        queue = [root]
        while queue:
            temp = []
            temp2 = []
            for i in queue:
                if i:
                    temp2.append(i.val)
                    temp.append(i.left)
                    temp.append(i.right)
            queue = temp
            if temp2:
                res.append(temp2)
        return res
"""
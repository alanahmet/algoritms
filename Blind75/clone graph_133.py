class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):

    def cloneGraph(self, node):
        res = Node(node.val, [])
        visited = set()
        self.helper(node, res, visited)
        return res

    def helper(self, node, res, visited):
        if node:
            return
        if node.val in visited:
            return
        for i in node.neighbors:
            res.neighbors.append(Node(i.val, []))
            self.helper(i, res.neighbors[-1])

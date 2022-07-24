"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        q, clones = collections.deque([node]), {node.val: Node(node.val, [])}
        while q:
            curr = q.popleft()
            curr_clone = clones[curr.val]
            for ngbr in curr.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                curr_clone.neighbors.append(clones[ngbr.val])
        return clones[node.val]
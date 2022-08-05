class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if r and l:
            return root
        return r or l
"""
class Solution:
    def lowestCommonAncestor(self, root: [TreeNode], p: [TreeNode], q: [TreeNode]) -> [TreeNode]:
        que = deque([root])
        parents = {root: None}
        ancestors = set()

        while q not in parents or p not in parents:
            node = que.popleft()

            if node.left:
                parents[node.left] = node
                que.append(node.left)

            if node.right:
                parents[node.right] = node
                que.append(node.right)

        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q

"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def maxPS(node):
            if not node: return 0

            l, r = max(0, maxPS(node.left)), max(0, maxPS(node.right))
            self.res = max(self.res, node.val + l + r)
            return node.val + max(l, r)

        maxPS(root)
        return self.res

class Solution:
    def isValidBST(self, root: []) -> bool:

        def valid(node, l, r):
            if not node:
                return True
            if not (l < node.val < r):
                return False
            return valid(node.left, l, node.val) and valid(node.right, node.val, r)

        return valid(root, float("-inf"), float("inf"))

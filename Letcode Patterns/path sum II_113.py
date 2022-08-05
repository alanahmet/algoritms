# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(np: [], node, s):  # node part, s:sums
            if s == targetSum and not node.left and not node.right:
                res.append(np)
                return
            if node.left:
                dfs(np + [node.left.val], node.left, s + node.left.val)  # Conflict
            if node.right:
                dfs(np + [node.right.val], node.right, s + node.right.val)  # Conflict

        dfs([root.val], root, root.val)
        return res

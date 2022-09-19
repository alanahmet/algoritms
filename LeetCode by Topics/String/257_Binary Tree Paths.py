# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(s, node):
            if not node.left and not node.right:
                ans.append(s + str(node.val))

            s += (str(node.val) + '->')
            if node.left:
                dfs(s, node.left)
            if node.right:
                dfs(s, node.right)
            return

        dfs(str(), root)
        return ans

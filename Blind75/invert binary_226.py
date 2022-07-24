# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: []) -> []:
        self.helper(root)

    def helper(self,root):
        if not root:
            return
        temp = root.right
        root.right = root.left
        root.left = temp
        self.helper(root.left)
        self.helper(root.right)


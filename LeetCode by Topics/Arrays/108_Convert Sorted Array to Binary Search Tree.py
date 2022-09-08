# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(i, j):
            if i > j:
                return None
            half = (i + j) // 2
            return TreeNode(nums[half], create(i, half - 1), create(half + 1, j))

        return create(0, len(nums) - 1)

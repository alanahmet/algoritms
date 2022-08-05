class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(i, j):
            if i > j:
                return None
            maxval = max(nums[i: j + 1])
            maxindex = nums.index(maxval)

            root = TreeNode(maxval)
            root.left = build(i, maxindex - 1)
            root.right = build(maxindex + 1, j)
            return root

        return build(0, len(nums) - 1)


"""my dummy
        res = TreeNode()
        def clm(ar, tree):
            if not ar: return

            mi = self.lmax(ar)
            tree.val = ar[mi]

            if len(ar) == 1: return

            if mi != len(ar) - 1:
                tree.right = TreeNode()
                clm(ar[mi + 1:], tree.right)

            if mi != 0:
                tree.left = TreeNode()
                clm(ar[:mi], tree.left)

        clm(nums, res)
        return res

    def lmax(self, arr):
        lm = 0
        for i in range(len(arr)):
            if arr[lm] < arr[i]:lm = i
        return lm

"""

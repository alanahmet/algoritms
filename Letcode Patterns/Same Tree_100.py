class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p or q.val is not p.val:
            return False
        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
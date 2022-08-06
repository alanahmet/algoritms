class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l, n, mw = 1, 1, 0  # level, num, max width
        q = deque([[l, n, root]])
        while q:
            [nl, nn, node] = q.popleft()
            if nl > l:
                l, n = nl, nn
            mw = max(mw, nn - n + 1)
            if node.left: q.append([nl + 1, nn * 2, node.left])
            if node.right: q.append([nl + 1, nn * 2 + 1, node.right])
        return mw

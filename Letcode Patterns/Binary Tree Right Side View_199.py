class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return[]
        q = collections.deque([root])
        res = []
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if i == len_q - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
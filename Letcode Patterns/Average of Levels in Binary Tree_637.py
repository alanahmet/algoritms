class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []
        curr_level = [root]
        res = []
        while curr_level:
            level_nodes = []
            next_level = []
            for node in curr_level:
                level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            res.append(sum(level_nodes) / len(level_nodes))
        return res
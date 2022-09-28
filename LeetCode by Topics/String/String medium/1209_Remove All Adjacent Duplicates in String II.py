class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i, v in enumerate(s):
            if not stack or stack[-1][0] != v:
                stack.append([v, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        return ''.join(v * r for v, r in stack)

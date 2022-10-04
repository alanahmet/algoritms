class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        for i, v in enumerate(expression):
            if v in '+-*':
                for a in self.diffWaysToCompute(expression[:i]):
                    for b in self.diffWaysToCompute(expression[i + 1:]):
                        ans.append(eval(str(a) + v + str(b)))

        return ans or [int(expression)]

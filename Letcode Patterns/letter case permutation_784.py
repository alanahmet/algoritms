class Solution:
    def letterCasePermutation(self, S) -> List[str]:
        res = ['']
        for s in S:
            if s.isalpha():
                res = [i + j for i in res for j in [s.upper(), s.lower()]]
            else:
                res = [i + s for i in res]
        return res

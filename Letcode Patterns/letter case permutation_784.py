class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 0: return []
        if len(s) == 1: return [s.upper(), s.lower()] if s.isalpha() else s
        res = []

        def backtrack(letter, s):
            if s == len(letter):
                res.append(letter)
                return
            if letter[s].isalpha():
                letter = letter[:s] + letter[s].upper() + letter[s + 1:]
                backtrack(letter, s + 1)
                letter = letter[:s] + letter[s].lower() + letter[s + 1:]
                backtrack(letter, s + 1)
                return
            backtrack(letter, s + 1)
            return

        backtrack(s, 0)
        return res

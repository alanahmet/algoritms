class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if len(digits) == 0: return []

        def bc(index, s):
            if index == len(digits):
                res.append(s)
                return
            for i in dic[digits[index]]:
                bc(index + 1, s + i)

        bc(0, "")
        return res

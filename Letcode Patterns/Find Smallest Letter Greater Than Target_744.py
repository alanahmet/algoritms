class Solution:
    def nextGreatestLetter(self, letters: [str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        return letters[0]

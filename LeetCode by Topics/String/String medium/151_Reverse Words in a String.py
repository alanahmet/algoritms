class Solution:
    def reverseWords(self, s: str) -> str:
        i, words = 0, []

        while i < len(s):
            word = ""
            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1
            if word:
                words.append(word)
            i += 1

        return " ".join(words[::-1])
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        used = [False] * 26
        counter = Counter(s)
        ans = []

        for c in s:
            counter[c] -= 1
            if used[ord(c) - ord('a')] == True:
                continue

            while ans and ans[-1] > c and counter[ans[-1]]:
                used[ord(ans[-1]) - ord('a')] = False
                ans.pop()

            ans.append(c)
            used[ord(c) - ord('a')] = True

        return "".join(ans)

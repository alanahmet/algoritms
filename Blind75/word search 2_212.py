class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        res = []

        def backtrack(s, r, c, i):
            if i == len(s) - 1:
                return True
            if not 0 <= r < len(board):
                return False
            if not 0 <= c < len(board[r]):
                return False
            if not s[i] == board[r][c]:
                return False
            return backtrack(s, r - 1, c, i + 1) or backtrack(s, r + 1, c, i + 1) or backtrack(s, r, c - 1,
                                                                                               i + 1) or backtrack(
                s, r, c + 1, i + 1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                word = board[i][j]
                for k in words:
                    if k[0] == word[0]:
                        if backtrack(k, i, j,0):
                            res.append(k)
                            break

        return res


board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
print(Solution().findWords(board, words))

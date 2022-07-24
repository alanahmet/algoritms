#"""""""""""""""""""""""""""
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        res = False
        for c in range(len(board)):
            for r in range(len(board[c])):
                if word[0] == board[c][r]:
                    if(self.backtrack(board, word, 0, c, r)):
                        return True
        return res

    def backtrack(self, board, word, index, c, r):
        if index == len(word) - 1:
            return True
        # top
        if c - 1 > -1:
            if board[c - 1][r] == word[index + 1]:
                return self.backtrack(board, word, index + 1, c - 1, r)

        # right
        if r + 1 < len(board[c]):
            if board[c][r + 1] == word[index + 1]:
                return self.backtrack(board, word, index + 1, c, r + 1)
        # left
        if r - 1 > -1:
            if board[c][r - 1] == word[index + 1]:
                return self.backtrack(board, word, index + 1, c, r - 1)
        # bottom
        if c + 1 < len(board):
            if board[c + 1][r] == word[index + 1]:
                return self.backtrack(board, word, index + 1, c + 1, r)
        return False
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, s: int) -> bool:
            if i < 0 or i == m or j < 0 or j == n:
                return False
            if board[i][j] != word[s] or board[i][j] == '*':
                return False
            if s == len(word) - 1:
                return True

            cache = board[i][j]
            board[i][j] = '*'
            isExist = \
                dfs(i + 1, j, s + 1) or \
                dfs(i - 1, j, s + 1) or \
                dfs(i, j + 1, s + 1) or \
                dfs(i, j - 1, s + 1)
            board[i][j] = cache
            return isExist

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
a = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")

"""
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        # print(board)
        m = len(board)
        n = len(board[0])
        k = len(word)

        if k > m * n:
            return False  # not enough letters

        # make sure that there are enough of each letter to be in the board
        wc = Counter(word)  # wc = word counter
        bc = Counter()  # bc = board counter
        for y, x in product(range(m), range(n)):
            bc[board[y][x]] += 1
        for ch in wc:
            if wc[ch] > bc[ch]:
                return False

        # now start with whichever side of the word has fewer possibilities
        # in the board
        if bc[word[0]] > bc[word[-1]]:
            word = word[::-1]  # reverse -- speedy way.

        ok_rc = lambda y, x: 0 <= y < m and 0 <= x < n

        # dfs...
        def search(r, c, pos, seen):
            # print('search ', r, c, pos, word[pos], board[r][c], seen)
            if pos == k - 1:
                return True
            seen.add((r, c))

            for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                rr = r + dy
                cc = c + dx
                if ((rr, cc) not in seen
                        and ok_rc(rr, cc)
                        and word[pos + 1] == board[rr][cc]
                ):
                    found = search(rr, cc, pos + 1, seen)
                    if found:
                        return True
            seen.remove((r, c))
            return False

        outside_seen = set()
        for y, x in product(range(m), range(n)):
            # print(y, x)
            if board[y][x] == word[0]:
                found = search(y, x, 0, outside_seen)
                if found:
                    return True
        return False
"""

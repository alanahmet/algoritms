class Solution:
    def bagOfTokensScore(self, tokens: [int], power: int) -> int:
        l, r, points = 0, len(tokens) - 1, 0
        tokens.sort()

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                points += 1
            elif points > 0 and l < r:
                power += tokens[r]
                r -= 1
                points -= 1

            else:
                break

        return points
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, count, l = 0, defaultdict(int), 0

        for i, v in enumerate(fruits):
            count[v] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            ans = max(ans, i - l + 1)
        return ans

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0] * (len(num1) + len(num2))

        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mult = int(num1[i]) * int(num2[j])
                summ = mult + ans[i + j + 1]
                ans[i + j + 1] = summ % 10
                ans[i + j] += summ // 10

        for i, v in enumerate(ans):
            if v != 0:
                break
        return ''.join(map(str, ans[i:]))

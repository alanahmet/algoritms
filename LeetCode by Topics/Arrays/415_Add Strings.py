class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry, res = 0, []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i])
            if j >= 0:
                carry += int(num2[j])
            res.append(str(carry % 10))
            carry //= 10
            i -= 1
            j -= 1

        return ''.join(reversed(res))

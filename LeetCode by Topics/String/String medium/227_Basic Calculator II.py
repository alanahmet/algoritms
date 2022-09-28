class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        s = s.replace(" ", "")
        num = 0

        while i < len(s):
            if i == 0:
                stack.append(int(s[i]))
            elif s[i - 1] == "+":
                stack.append(int(s[i]))
            elif s[i - 1] == "-":
                stack.append(-int(s[i]))
            elif s[i] == "*":
                stack[-1] *= int(s[i + 1])
                i += 1
            elif s[i] == "/":
                stack[-1] //= int(s[i + 1])
                i += 1
            i += 1

        return sum(stack)

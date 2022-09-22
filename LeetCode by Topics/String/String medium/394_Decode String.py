class Solution:
    def decodeString(self, s: str) -> str:
        stack, curNum, curStr = [], 0, ''
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                if c == '[':
                    stack.append((curNum, curStr))
                    curStr = ''
                    curNum = 0
                elif c == ']':
                    num, prevStr = stack.pop()
                    curStr = prevStr + curStr * num
                else:
                    curStr += c

        return curStr

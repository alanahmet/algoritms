class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for i in s:
            if i.isalpha() or i.isalnum():
                clean_s+=i.lower()

        print(clean_s)
        for i in range(len(clean_s)//2):
            if not clean_s[i] == clean_s[-(i+1)]:
                return False
        return True

a = Solution().isPalindrome("0P")
print(a)
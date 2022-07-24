class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(a):
            if a == 0:
                return 1
            if a == 1:
                return 1
            return fib(a-2) + fib(a-1)
        return fib(n)



"""     
        self.stair = 0
        def backtrack(self,s):
            if s == 0:
                self.stair += 1
            if s < 0:
                return
            backtrack(self,s - 1)
            backtrack(self,s-2)
        backtrack(self,n)
        return self.stair"""

Sol = Solution()
sol = Sol.climbStairs(35)
print(sol)
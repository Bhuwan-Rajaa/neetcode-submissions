class Solution:
    def climbStairs(self, n: int) -> int:
        res = [-1] * n
        def dp(i):
            if i >= n:
                return 1 if i == n else 0
            if res[i] != -1:
                return res[i]
            res[i] = dp(i+1) + dp(i+2)

            return res[i]
        
        return dp(0)

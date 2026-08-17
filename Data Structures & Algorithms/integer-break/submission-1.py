class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        def dfs(i):
            if i in dp:
                return dp[i] 
            dp[i] = 0 if i == n else i
            for num in range(1,i):
                val = dfs(num) * dfs(i-num)
                dp[i] = max(val,dp[i])

            return dp[i]
        return dfs(n)
                    

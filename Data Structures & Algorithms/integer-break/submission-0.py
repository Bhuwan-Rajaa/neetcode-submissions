class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1
        arr = [2,3,5,7]
        
        def dfs(i):
            if dp[i] != -1:
                return dp[i] 
            
            for num in arr:
                if i-num>=0:
                    dp[i] = max(dp[i], dfs(i-num)*num)

        dfs(n)
        return dp[n]
                    

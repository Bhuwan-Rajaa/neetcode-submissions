class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * amount
        
        def dfs(i):
            if i == amount:
                return 
            
            for c in coins:
                if i+c<= amount:
                    if dp[i+c] != -1:
                        return dp[i+c]
                    dfs(i+c)

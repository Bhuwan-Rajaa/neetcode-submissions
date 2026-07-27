class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        l = sum(matchsticks) // 4
        sq = [0,0,0,0]
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for s in range(4):
                if sq[s] + matchsticks[i] <= l:
                    sq[s] += matchsticks[i]
                    if dfs(i+1):
                        return True
                if sq[s] == 0:
                    break
            return False
        return dfs(0)

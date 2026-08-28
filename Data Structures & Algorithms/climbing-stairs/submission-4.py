class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 2
        sup = 1
        if n<2:
            return 1
        for i in range(n-2):
            temp = ans
            ans = ans + sup
            sup = temp
        
        print(ans)
        return ans
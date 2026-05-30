class Solution:
    def myPow(self, x: float, n: int) -> float:
        np = abs(n)
        if x == 0:
            return 0
        if x == 1 or n == 0:
            return 1

        res = 1
        for i in range(np):
            res *= x


        return res if np == n else 1/res
        

class Solution:
    def numSquares(self, n: int) -> int:
        res = 0

        while n:
            n = n - (math.floor(math.sqrt(n))**2)
            res += 1

        return res
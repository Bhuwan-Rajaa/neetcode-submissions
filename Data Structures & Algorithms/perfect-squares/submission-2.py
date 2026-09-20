class Solution:
    def numSquares(self, n: int) -> int:


        def isSquareNum(num):
            s = int(math.sqrt(num))
            return s * s == num

        if isSquareNum(n):
            return 1

        i = 1
        while i * i <= n:
            if isSquareNum(n - i * i):
                return 2
            i += 1

        return 3
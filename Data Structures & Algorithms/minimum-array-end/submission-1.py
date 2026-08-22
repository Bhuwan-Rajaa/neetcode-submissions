class Solution:
    def minEnd(self, n: int, x: int) -> int:
        diff = 1
        for i in range(1,32):
            if x <= diff:
                break
            diff *= 2

        return x+diff*(n-1)
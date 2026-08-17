class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = right
        for i in range(left,right):
            res &= i
        return res
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        seen = set(nums)

        while res in seen:
            res += 1
        
        return res
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0

        while r<len(nums):
            farthest = r
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            r = farthest
            l = r+1
            res+=1
        
        return res
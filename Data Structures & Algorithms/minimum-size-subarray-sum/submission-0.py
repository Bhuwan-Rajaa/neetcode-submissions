class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = 100001
        cursum = 0
        l = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum >= target:
                minlen = min(minlen, r-l+1)        
                cursum -= nums[l]
                l+=1
            
        return minlen if minlen != 100001 else 0
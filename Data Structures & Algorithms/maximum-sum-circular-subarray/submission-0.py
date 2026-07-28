class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax,gmin = nums[0],nums[0]

        cmax = 0
        cmin = 0
        total = 0

        for num in nums:
            cmax = max(cmax + num,num)
            cmin = min(cmin+num,num)
            total+=num
            gmax = max(gmax,cmax)
            gmin = min(gmin,cmin)
        
        return max(gmax,total-gmin) if gmax > 0 else gmax
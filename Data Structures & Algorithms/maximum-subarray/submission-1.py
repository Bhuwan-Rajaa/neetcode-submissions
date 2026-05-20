class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''cur = 0
        maxs = nums[0]

        for num in nums:
            if cur<0:
                cur = 0
            cur += num
            maxs = max(maxs,cur)
        
        return maxs'''

        dp = [*nums]
        for i in range(1,len(dp)):
            dp[i] = max(dp[i] , nums[i]+dp[i-1])
        
        return max(dp)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = nums[0]
        l,r = 0,len(nums)-1
        res = 1000

        while l<r:
            m = (l+r)//2

            if nums[m] > left:
                l = m+1
                res = min(res,nums[m])

            else: 
                r = m
                res = min(res,nums[m])

        return nums[l]
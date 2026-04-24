class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        return l

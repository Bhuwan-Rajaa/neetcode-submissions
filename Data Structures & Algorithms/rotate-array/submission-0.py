class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = k

        for _ in range(n-k):
            nums[l],nums[r%n] = nums[r%n], nums[l]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0'''

        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                return False
            i += nums[i]
            print(i)
        if i == len(nums)-1:
            return True
        return False
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(nums, cur, index):
            if index == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[index])
            backtrack(nums, cur, index +1)
            cur.pop()
            backtrack(nums, cur, index+1)

        backtrack(nums,cur,0)
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subs = []

        def dt(idx):
            if idx >= len(nums):
                res.add(subs.copy())
                return
            subs.append(nums[idx])
            dt(idx+1)
            subs.pop()
            dt(idx+1)

        dt(0)
        return list(res)
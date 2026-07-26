class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subs = []
        res = []
        def bt(i):
            if i == len(nums):
                return
            
            if sum(subs)>target:
                return
            
            if sum(subs)== target:
                if subs not in res:
                    res.append(subs.copy())

            subs.append(nums[i])
            bt(i)
            subs.pop()
            bt(i+1)
        
        bt(0)

        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subs = []
        res = []
        nums = candidates
        def bt(i):
            if i == len(nums):
                return
            
            if sum(subs)>target:
                return
            
            if sum(subs)== target:
                if subs not in res:
                    res.append(subs.copy())

            subs.append(nums[i])
            bt(i+1)
            subs.pop()
            bt(i+1)
        
        bt(0)

        return res
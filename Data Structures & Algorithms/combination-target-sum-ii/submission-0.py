class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        cur = []

 
            
        def backtrack(cur , index, csum):
            if csum == target:
                res.append(cur.copy())
                return
            if index == len(nums) or csum > target:
                return

            
            cur.append(nums[index])
            backtrack(cur,index+1,csum+nums[index])
            cur.pop()
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                i+=1

            backtrack(cur, index+1, csum)
                
        backtrack(cur, 0, 0)
        return res
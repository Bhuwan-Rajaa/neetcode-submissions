class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(cur , index, csum):
            if csum == target:
                res.append(cur.copy())
                return
            if index == len(nums) or csum > target:
                return

            
            cur.append(nums[index])
            backtrack(cur,index,csum+nums[index])
            cur.pop()
            backtrack(cur, index+1, csum)
                
        backtrack(cur, 0, 0)
        return res
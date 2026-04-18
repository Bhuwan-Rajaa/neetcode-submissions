class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
        
        def backtrack(index, cur):
            if index == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[index])
            backtrack(index+1, cur)
            cur.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index+=1
                    
            backtrack(index+1, cur)
        
        backtrack(0,cur)
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False for _ in range(len(nums))]

        temp = []
        res = []

        def permute():
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for i in range(len(nums)):
                num = nums[i]
                if not used[i]:
                    used[i] = True
                    temp.append(num)
                    permute()
                    used[i] = False
                    temp.pop()
            
            return
            
        permute()
        return res
                



            
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def bt(i,s):
            nonlocal res
            xor = 0

            for num in s:
                xor ^= num
            
            res += xor

            for j in range(i,len(nums)):
                s.append(nums[j])
                bt(j+1,s)
                s.pop()
            
        bt(0,[])
        return res
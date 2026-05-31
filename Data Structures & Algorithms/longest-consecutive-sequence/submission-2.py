class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = set(nums)

        res = 0

        for num in present:
            length = 1
            while num+length in present:
                length +=1
            res = max(res,length)
        return res
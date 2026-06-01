class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        df = defaultdict(int)

        for num in nums:
            df[num] += 1
        maxc = 0
        res = 0
        for num,freq in df.items():
            if maxc < freq:
                maxc = freq
                res = num
        
        return res

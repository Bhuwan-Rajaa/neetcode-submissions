class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        df = defaultdict(int)
        tar = len(nums)/3.0
        res = []
        for num in nums:
            df[num] += 1
        
        for num,freq in df.items():
            if freq > tar:
                res.append(num)

        return res
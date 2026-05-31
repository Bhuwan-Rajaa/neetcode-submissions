class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        df = defaultdict(list)
        freq = [[]for _ in range(len(nums)+1)]
        for num in nums:
            df[num] = 1 + df.get(num,0)
        
        for n,c in df.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
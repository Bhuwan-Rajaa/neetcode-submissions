class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ca = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            ca[i] = 1 + ca.get(i , 0)
        for n,i in ca.items():
            freq[i].append(n)

        result = []
        for i in range(len(freq) -1, 0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        
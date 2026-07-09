class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        df = {}

        for i,num in enumerate(nums):
            if num in df:
                j = df[num]
                if abs(i-j) <= k:
                    return True
            df[num] = i
            
        return False
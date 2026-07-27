class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) %k != 0:
            return False

        t = sum(nums) // k
        nums.sort(reverse = True)

        used = [False] * len(nums)

        def bt(i,k,ss):
            if k == 0:
                return True
            
            if ss == t:
                return bt(0,k-1,0)
            
            for j in range(i,len(nums)):
                if not used[j] and ss + nums[j] <= t:
                    used[j] = True
                    if bt(j+1,k,ss+nums[j]):
                        return True
                    used[j] = False
                if not used[j] and ss == 0:
                    return False
                
            return False
        
        return bt(0,k,0)
                


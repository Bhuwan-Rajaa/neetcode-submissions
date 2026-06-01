class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        df = {0:0, 1:0, 2:0}

        for num in nums:
            if num == 0:
                df[0] +=1
            elif num == 1:
                df[1] +=1
            else:
                df[2] += 1
        i = 0
        for u,freq in df.items():
            while freq:
                nums[i] = u
                freq -= 1
                i+=1
            
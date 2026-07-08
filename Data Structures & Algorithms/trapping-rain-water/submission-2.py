class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        water = 0
        lm = height[l]
        rm = height[r]

        while l<r:
            if lm<rm:
                l+=1
                lm = max(lm,height[l])
                water+=lm-height[l]

            else:
                r-=1
                rm = max(rm,height[r])
                water+= rm-height[r]
            
        return water
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 0
        water = 0
        maxh = 0
        while r<len(height):
            if maxh <= height[r]:
                while l<r:
                    water += maxh - height[l]
                    l+=1
                maxh = height[r]
                r+=1
                l = r
                print(water,maxh)
            else:
                r+=1
    
        return water

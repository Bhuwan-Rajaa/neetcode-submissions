class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights)-1
        i = 0
        j = 0

        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            if res<area:
                res = area
                i = l
                j = r
            
            if heights[l]<= heights[r]:
                l+=1
            else:
                r-=1
        print(i,j)        
        return res

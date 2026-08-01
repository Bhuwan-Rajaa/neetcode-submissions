class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mheap = []
        for x,y in points:
            dist = -(x*x + y*y)
            heapq.heappush(mheap,[dist,x,y])
            if len(mheap) > k:
                heapq.heappop(mheap)
            
            res = []
        while mheap:
            d,x,y = heapq.heappop(mheap)
            res.append([x,y])
        
        return res
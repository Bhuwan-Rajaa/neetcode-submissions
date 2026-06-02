import heapq

class Solution:
    def merge(self, nums1, m, nums2, n):

        heap = nums1[:m]

        heapq.heapify(heap)

        for x in nums2:
            heapq.heappush(heap, x)

        for i in range(m + n):
            nums1[i] = heapq.heappop(heap)
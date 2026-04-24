class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2
        if len(a)>len(b):
            a,b = b,a

        al= len(a)
        bl = len(b)
        total = al+bl
        half = total//2

        l,r = 0,al-1

        while True:
            m1 = (l+r)//2
            m2 = half-m1-2

            aleft = a[m1] if m1 >= 0 else float("-infinity")
            aright = a[m1+1] if m1+1 < al else float("infinity")
            bleft = b[m2] if m2 >= 0 else float("-infinity")
            bright = b[m2+1] if m2+1 < bl else float("infinity")

            if aleft <= bright and bleft <= aright:
                if total%2 == 0:
                    return (max(aleft,bleft) + min(aright,bright)) /2
                return min(aright,bright)
            
            elif aleft > bright:
                r = m1-1
            else:
                l = m1
    
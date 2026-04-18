from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            # compute hours needed at rate mid
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid  # integer ceil(p / mid)
                if hours > h:                 # small early stop
                    break

            if hours <= h:
                high = mid    # mid is feasible, try lower
            else:
                low = mid + 1 # mid too slow, raise speed

        return low

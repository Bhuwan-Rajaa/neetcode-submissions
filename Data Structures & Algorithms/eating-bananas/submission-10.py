class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kr = max(piles)
        kl = 1
        res = kr

        while kl < kr:
            k = (kl+kr)//2
            
            t = 0
            for i in piles:
                t+= math.ceil(float(i)/k)

            if t > h:
                kl = k+1
            elif t<=h:
                res = k
                kr = k
                

        return res
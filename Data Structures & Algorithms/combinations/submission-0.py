class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subs = []

        def dt(idx):
            if len(subs) == k:
                res.append(subs.copy())
                return
            if idx >n:
                return
            
            subs.append(idx)
            dt(idx+1)
            subs.pop()
            dt(idx+1)
        
        dt(1)
        return res


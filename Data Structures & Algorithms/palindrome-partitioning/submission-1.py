class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def ispali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True


        def dfs(i):
            if i >= len(s):
                res.append(p.copy())
                return
            
            for j in range(i,len(s)):
                if ispali(i,j):
                    p.append(s[i:j+1])
                    dfs(j+1)
                    p.pop()
        
        p = []
        res = []
        dfs(0)
        return res
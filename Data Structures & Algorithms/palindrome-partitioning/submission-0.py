class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        par = []

        def backtrack(index):
            if index == len(s):
                res.append(par.copy())
                return

            for j in range(index, len(s)):
                if self.ispar(s, index, j):
                    par.append(s[index:j+1])
                    backtrack(j + 1)
                    par.pop()

        backtrack(0)
        return res

    def ispar(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

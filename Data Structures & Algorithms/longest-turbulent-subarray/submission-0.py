class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur = 0
        gmax = 0
        i = 0

        while i < len(arr) - 1:
            if arr[i] % 2 == 1:
                if arr[i+1] %2 == 0:
                    cur += 2
                    gmax = max(gmax,cur)
                    i+=2
                else:
                    cur = 0
                    i += 1
            else:
                if arr[i+1] % 2 == 1:
                    cur += 2
                    gmax = max(gmax,cur)
                    i += 2
                else:
                    cur = 0
                    i+=1

        return gmax



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            k1 = k
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                else:
                    if k1 > 0:
                        count+=1
                        k1-=1
                    else:
                        count = 0
                        k1 = k
                res = max(res,max(count+k1,len(s)))

        return res
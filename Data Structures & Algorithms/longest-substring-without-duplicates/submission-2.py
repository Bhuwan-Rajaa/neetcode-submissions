class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lsubs = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in lsubs:
                lsubs.remove(s[l])
                l+=1
            lsubs.add(s[r])
            longest = max(longest, r-l+1)
        return longest
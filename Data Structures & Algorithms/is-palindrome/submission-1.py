class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        return s == s[::-1]

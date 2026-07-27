class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        dtc = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def bt(i,cur):
            if i == n:
                res.append(cur)
                return
            
            for c in dtc[digits[i]]:
                bt(i+1, cur+c)
        if digits:
            bt(0,"")
        return res
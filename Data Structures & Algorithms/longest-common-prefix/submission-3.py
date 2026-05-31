class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for st in strs:
            if st == '':
                return ''
            for i,c in enumerate(st):
                if i >= len(prefix):
                    continue
                if c != prefix[i]:
                    if i == 0:
                        prefix = ""
                    prefix = prefix[:i]


        return prefix
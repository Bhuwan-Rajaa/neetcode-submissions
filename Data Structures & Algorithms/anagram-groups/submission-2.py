
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        df = defaultdict(list)

        for stri in strs:
            count = [0]*26
            for c in stri:
                count[ord(c)-ord('a')]+= 1
            df[tuple(count)].append(stri)
        return list(df.values())
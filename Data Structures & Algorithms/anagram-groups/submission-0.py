class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        df = defaultdict(list)
        for stg in strs:
            count = [0] * 26
            for char in stg:
                count[ord(char)- ord('a')]+=1
            df[tuple(count)].append(stg)

        return (list(df.values()))
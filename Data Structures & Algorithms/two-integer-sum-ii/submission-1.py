class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while j>i:
            s1 = numbers[i] + numbers[j]

            if s1>target:
                j-=1
            elif s1<target:
                i+=1
            else:
                return[1+i, 1+j]
        
        return []
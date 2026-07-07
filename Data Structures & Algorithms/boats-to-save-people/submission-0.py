class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        a = sum(people)//limit
        if sum(people) % limit:
            a+=1
        
        return a
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0

        r = len(people)-1
        res = 0
        while l<= r:
            rem = limit - people[r]
            res +=1
            r-=1
            while l<= r and rem >= people[l]:
                rem -= people[l]
                l+=1
            
        return res

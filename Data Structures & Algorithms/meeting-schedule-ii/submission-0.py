"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start,end = [], []
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])


        s = 0
        e = 0
        rn = 0
        tot = 0
        while s<len(start) and e<len(start):
            if start[s] >= end[e]:
                rn-=1
                e+=1
                
            else:
                rn+=1
                tot = max(tot,rn)
                s+=1

        return tot
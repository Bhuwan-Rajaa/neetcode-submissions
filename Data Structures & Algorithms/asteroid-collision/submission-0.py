class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while a<0 and stk and stk[-1] > 0:
                d = a + stk[-1]
                if d>0:
                    a = 0
                elif d<0:
                    stk.pop()
                else:
                    a = 0
                    stk.pop()
            if a:
                stk.append(a)
            
        return stk
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t = 0,0
        for bil in bills:
            if bil == 5:
                f+=1
            elif bil == 10:
                t+=1
                f-=1
            elif t:
                t-=1
                f-=1
            else:
                f-=3

            if f<0:
                return False
        return True
        
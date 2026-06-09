class Solution:
    def isValid(self, s: str) -> bool:
        b1,b2,b3 = 0,0,0
        for c in s:

            if c == '(':
                b1+=1
            elif c == ')':
                b1-=1
            elif c == '{':
                b2+=1
            elif c == '}':
                b2-=1
            elif c == '[':
                b3+=1
            elif c == ']':
                b3-=1
        
        return (b1==0 and b2==0 and b3 == 0)
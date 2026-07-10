class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        close = ("}","]",")")
        for i in s:
            if i in close:
                if i == ')' and stk[-1] == '(':
                    stk.pop()
                elif i == '}' and stk[-1] == '{':
                    stk.pop()
                elif i == ']' and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return True
        

                

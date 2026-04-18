class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        cto = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in cto:
                if stk and stk[-1] == cto[i]:
                    stk.pop()
                else:
                    return False
                
            else: stk.append(i)

        return True if not stk else False
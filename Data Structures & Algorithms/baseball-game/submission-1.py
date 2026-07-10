class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i in operations:
            if i == '+':
                stk.append(int(stk[-1])+int(stk[-2]))
            elif i == 'C':
                stk.pop()
            elif i == 'D':
                stk.append(2*int(stk[-1]))
            else:
                stk.append(int(i))

        return sum(stk)
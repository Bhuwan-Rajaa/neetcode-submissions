class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stk1)-1):
            self.stk2.append(self.stk1.pop())
        temp = self.stk1.pop()
        for _ in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop())
        return temp
    def peek(self) -> int:
        return self.stk1[0]

    def empty(self) -> bool:
        return not self.stk1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
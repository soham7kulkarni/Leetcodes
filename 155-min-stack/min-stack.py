class MinStack:

    def __init__(self):
        self.min = sys.maxsize
        self.st = []

    def push(self, val: int) -> None:
        if val <= self.min:
            self.st.append(self.min)
            self.min = val
        self.st.append(val)
    def pop(self) -> None:
        if self.min == self.st.pop():
            self.min = self.st.pop()
    def top(self) -> int:
        return self.st[-1]
    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
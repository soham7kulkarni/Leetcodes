class MinStack:

    def __init__(self):
        self.st = []
        self.min = sys.maxsize

    def push(self, value: int) -> None:
        if value <= self.min:
            self.st.append(self.min)
            self.min = value
        self.st.append(value)

    def pop(self) -> None:
        if self.min == self.st.pop():
            self.min = self.st.pop()


    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
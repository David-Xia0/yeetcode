class MinStack:

    def __init__(self):
        self.arr = []
        self.smol = []

    def push(self, val: int) -> None:
        if len(self.smol) == 0:
            self.smol.append(val)
        else:
            self.smol.append(min(val, self.smol[-1]))
        self.arr.append(val)
        
    def pop(self) -> None:
        self.arr.pop()
        self.smol.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.smol[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
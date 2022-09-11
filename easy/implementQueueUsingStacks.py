from queue import Empty


class MyQueue:

    def __init__(self):
        self.b = []
        self.f = []

    def push(self, x: int) -> None:
        if len(self.f) != 0:
            while len(self.f) != 0:
                self.b.append(self.f.pop())
        self.b.append(x)


    def pop(self) -> int:
        if len(self.b) != 0:
            while len(self.b) != 0:
                self.f.append(self.b.pop())
        return self.f.pop()
        

    def peek(self) -> int:
        if len(self.b) != 0:
            while len(self.b) != 0:
                self.f.append(self.b.pop())
        
        return self.f[-1]
        

    def empty(self) -> bool:
        return len(self.b) == 0 and len(self.f) == 0
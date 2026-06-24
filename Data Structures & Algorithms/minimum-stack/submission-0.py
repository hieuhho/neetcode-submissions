class MinStack:

    def __init__(self):
        self.minStack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.minVal:
            self.minVal.append(min(self.minVal[-1], val))
        else:
            self.minVal.append(val)
        
    def pop(self) -> None:
        self.minStack.pop()
        self.minVal.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
        

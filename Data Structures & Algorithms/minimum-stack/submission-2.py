class MinStack:

    def __init__(self):
        self.minStack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        minVal = min(self.minVal[-1] if self.minVal else val, val)
        self.minVal.append(minVal)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
class MyQueue:
    
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
    
    def push(self, x: int) -> None:
        self.push_stack.append(x)
    
    def pop(self) -> int:
        if not self.pop_stack:
            self._transfer()
        
        return self.pop_stack.pop()
    
    def peek(self) -> int:
        if not self.pop_stack:
            self._transfer()
        
        return self.pop_stack[-1]
    
    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack
    
    def _transfer(self) -> None:
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())

if __name__ == "__main__":
    myQueue = MyQueue()
    
    myQueue.push(1)
    myQueue.push(2)
    
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())
    
    myQueue.push(3)
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.empty())
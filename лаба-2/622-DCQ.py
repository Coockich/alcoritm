class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * k
        self.front = -1
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k
        
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.k
        
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    
    print(myCircularQueue.enQueue(1))
    print(myCircularQueue.enQueue(2))
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.enQueue(4))
    
    print(myCircularQueue.Rear())
    print(myCircularQueue.isFull())
    
    print(myCircularQueue.deQueue())
    print(myCircularQueue.enQueue(4))
    
    print(myCircularQueue.Rear())

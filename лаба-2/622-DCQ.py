class MyCircularQueue:

    def __init__(self, k: int):
        """
        Инициализирует круговую очередь с максимальным размером k
        """
        self.k = k                    # максимальный размер очереди
        self.queue = [0] * k          # массив фиксированного размера
        self.front = -1               # индекс первого элемента (-1 = пусто)
        self.rear = -1                # индекс последнего элемента (-1 = пусто)
        self.count = 0                # текущее количество элементов

    def enQueue(self, value: int) -> bool:
        """
        Вставляет элемент в конец очереди
        Возвращает True если успешно, иначе False
        """
        if self.isFull():
            return False
        
        if self.isEmpty():
            # Если очередь пуста, front и rear указывают на один элемент
            self.front = 0
            self.rear = 0
        else:
            # Иначе двигаем rear по кругу
            self.rear = (self.rear + 1) % self.k
        
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Удаляет элемент из начала очереди
        Возвращает True если успешно, иначе False
        """
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            # Если в очереди был один элемент, после удаления она становится пустой
            self.front = -1
            self.rear = -1
        else:
            # Иначе двигаем front по кругу
            self.front = (self.front + 1) % self.k
        
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Возвращает первый элемент очереди
        Если очередь пуста, возвращает -1
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Возвращает последний элемент очереди
        Если очередь пуста, возвращает -1
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Проверяет, пуста ли очередь
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Проверяет, заполнена ли очередь
        """
        return self.count == self.k


# Пример использования
if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    
    print(myCircularQueue.enQueue(1))  # True
    print(myCircularQueue.enQueue(2))  # True
    print(myCircularQueue.enQueue(3))  # True
    print(myCircularQueue.enQueue(4))  # False (очередь заполнена)
    
    print(myCircularQueue.Rear())      # 3
    print(myCircularQueue.isFull())    # True
    
    print(myCircularQueue.deQueue())   # True (удаляем 1)
    print(myCircularQueue.enQueue(4))  # True (добавляем 4)
    
    print(myCircularQueue.Rear())
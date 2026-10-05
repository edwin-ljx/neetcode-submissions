class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.size = 0
            self.capacity = capacity
            self.arr = [0] * capacity
            

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for index,el in enumerate(self.arr):
            new_arr[index] = el
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
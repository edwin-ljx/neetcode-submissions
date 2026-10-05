class Node:

    def __init__(self,val,next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.size += 1
        


    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        curr = self.head  # start at dummy

        for _ in range(index):
            curr = curr.next

        to_delete = curr.next
        curr.next = to_delete.next

        if index == self.size - 1:
            self.tail = curr

        self.size -= 1
        return True
            


    def getValues(self) -> List[int]:
        res = []
        i = 0
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


        

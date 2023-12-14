class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def printt(self):
        if self.head is None:
            print("Empty List!")
            return
        h = self.head
        while h is not None:
            print(f"{h.data} ->", end=" ")
            h = h.next
        print("Null")

if __name__ == '__main__':
    L = LinkedList()
    L.insert(20)
    L.insert(15)
    L.insert(10)
    L.printt()
            
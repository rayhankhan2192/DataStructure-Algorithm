class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertvalue(self, dataList):
        self.head = None
        for data in dataList:
            node = Node(data, self.head)
            self.head = node
    
    #Delection operation
    def remove(self, position):
        if position < 0 or position >= self.length():
            raise Exception("Out of Bounds")

        if position == 0:
            self.head = self.head.next
            return

        count = 0
        h = self.head
        while h:
            if count == position - 2:
                h.next = h.next.next
                break
            h = h.next
            count += 1

    #lenght of the linked list
    def length(self):
        h = self.head
        length = 0
        while h:
            length += 1
            h = h.next
        return length
    
    #Traverse the Linked List      
    def printf(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            h = self.head
            while h is not None:
                print(f"{h.data} ->", end=" ")
                h = h.next
        print("NULL")
        
if __name__ == '__main__':
    List = LinkedList()
    
    List.insertvalue([50, 40, 30, 20, 10])
    List.printf()
    print(f"\nLength: {List.length()}")
    List.remove(2)
    print("\n")
    List.printf()
    print(f"\nLength: {List.length()}\n")
class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # insert at the end
    def append_Al_Last(self, data):
        if self.head is None:
            node = Node(data)
            node.prev = None  # make sure previous node point to the none, this is the first value
            self.head = node
            return
        h = self.head
        node = Node(data)  # create a new node
        while h.next:
            h = h.next
        h.next = node  # insert the new data into new created node
        node.prev = h  # last node is point to the previous node
        node.next = None  # 4last node is point to the Null/None

    #insert at the beginning
    def prepend_At_First(self, data):
        if not self.head:
            node = Node(data)
            node.prev = None
            self.head = node
            return
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node
        node.prev = None
    
    # add new value after the specific value    
    def add_after_value(self, key, data):
        h = self.head
        while h is not None:
            if h.next is None and h.data == key:
                self.append_Al_Last(data)
                return
            elif h.data == key:
                node = Node(data)
                next = h.next #store next node, from corrent
                h.next = node
                node.next = next #now new node points to the next node, which i stored, its linked with newnode to next node
                node.prev = h
                next.prev = node
                return
            h = h.next
            
    # add new value before the specific value 
    def add_before_value(self, key, data):
        h = self.head
        while h is not None:
            if h.prev is None and h.data == key:
                self.prepend_At_First(data)
                return
            elif h.data == key:
                node = Node(data)
                prev = h.prev
                prev.next = node
                h.prev = node
                node.next = h
                node.prev = prev
            h = h.next
            
    def remove(self, value):
        h = self.head
        while h:
            if h.data == value:
                #This is not the first NODE(not head) (make the Forward connection)
                if h.prev:
                    h.prev.next = h.next
                #if the value is the head
                else:
                    self.head = h.next
                #This is not the last NODE(make the backward connection)
                if h.next:
                    h.next.prev = h.prev
                #remove the current garbage
                h.prev = None
                h.next = None
                return True
            h = h.next
                
    #print first to last
    def printForward(self):
        h = self.head
        if self.head is None:
            print("Empty Linked list!")
            return
        while h:
            print(f"{h.data}->", end=" ")
            h = h.next
        print("NULL")
    
    #print last to first
    def prontbackward(self):
        h = self.head
        while h and h.next :
            h = h.next
        while h:
            print(f"{h.data}->", end=" ")
            h = h.prev
        print("Null")


if __name__ == '__main__':
    l = LinkedList()
    l.append_Al_Last(10)
    l.append_Al_Last(20)
    l.append_Al_Last(40)
    l.append_Al_Last(50)
    l.prepend_At_First(5)
    l.add_after_value(20, 30)
    l.add_before_value(20, 15)
    
    l.remove(50)
    l.remove(20)
    l.remove(5)
    
    
    l.printForward()
    l.prontbackward()

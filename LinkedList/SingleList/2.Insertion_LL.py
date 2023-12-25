class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, data):
        #create a instance of Node and
        #initializing it with the provided data value and setting its next attribute to the current head of the linked list. 
        # The new node is now pointing to the previous head of the list.
        node = Node(data, self.head)
        self.head = node # Update the head of the linked list to the newly created node
     
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        h = self.head
        while h.next:
            h = h.next
        h.next = Node(data, None)
        
    #insert with index    
    def insertAt(self, index, data):
        if index < 0 and index > self.length():
            raise Exception("Out of bounds!")
        if index == 0:
            self.insertAtBeginning(data)
            return
        count = 0
        h = self.head
        while h:
            if count == index-1:
                node = Node(data, h.next)
                h.next = node
                break 
            h = h.next
            count += 1
        
    
    #insert value from List   
    def insertValue(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)
            #self.insertAtBeginning(data)
            
            
    #length of the linked List
    def length(self):
        length = 0
        h = self.head
        while h:
            length += 1
            h = h.next
        return length
        
    def PrintItems(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            h = self.head
            while h is not None:
                print(f"{h.data} ->", end=" ")
                h = h.next
            print("Null")
            
if __name__ == '__main__':
    List = LinkedList()
    
    # List.insertAtBeginning(10)
    # List.insertAtBeginning(20)
    # List.insertAtBeginning(30)
    # List.insertAtBeginning(40)
    # List.insertAtBeginning(50)
    # List.insertAtEnd(5)
    # List.insertAtBeginning(10)
    
    List.insertValue([10, "Ten", 20, "Twenty", 30, "Thirty"])
    List.insertAt(1, "TWO")
    List.PrintItems()
    
    print(f"Length: {List.length()}")
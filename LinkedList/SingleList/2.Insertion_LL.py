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
    List.insertAtBeginning(10)
    List.insertAtBeginning(20)
    List.insertAtBeginning(30)
    List.insertAtBeginning(40)
    List.insertAtBeginning(50)
    List.insertAtEnd(5)
    List.insertAtBeginning(10)
    List.PrintItems()
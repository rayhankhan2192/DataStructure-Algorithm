class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
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
    List.PrintItems()
#Basic build of Linked List, actually how its work.

class Node:
    def __init__(self, data = None, next = None):
        self.data = data #contain data
        self.next = next #pointer to the next element
        
#creating node
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

#Connecting Node
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

if __name__ == '__main__':
    head = a
    while head is not None:
        print(f"head: {id(head)} Data: {head.data} ->", end=" ")
        head = head.next
        print(f"next: {id(head)}")
    print("Null")
    
    # while head is not None:
    #     print(f"{head.data}->", end=" ")
    #     head = head.next
    # print("Null")
from array import *
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# arr = array('i', [0]*20)
arr = array('i', [1, 2, 3, 4, 5])
arr.extend([0] * (10-len(arr)))

# insertion operation
def insertion(arr, index, value):
    if (index < 0 or index > len(arr)):
        print("Array out of bounds")
    for i in range(len(arr)-1, index-1, -1):
        arr[i] = arr[i-1]
    arr[index-1] = value
    
    
print("Before Insertion: ",arr)
while (1):
    index = int(input("\nEnter the Position to Insert: "))
    value = int(input("Enter the value to Insert   : "))
    insertion(arr, index, value)
    print("After Insertion: ", arr)

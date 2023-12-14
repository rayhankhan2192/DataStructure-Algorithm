from array import *
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# arr = array('i', [0]*20)
arr = array('i', [1, 2, 3, 4, 5])
arr.extend([0] * (10-len(arr)))

# delection operation
def delection(arr, index):
    if (index < 0 or index > len(arr)):
        print("Array out of bounds")
    for i in range(index-1, len(arr)-1):
        arr[i] = arr[i+1]
print("Before Delection: ",arr)
while (1):
    index = int(input("Enter the Position to Delete: "))
    delection(arr, index)
    print("After Delection: ", arr)
    print("\n")

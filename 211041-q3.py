def AddNode(arr, root, free):
    if free == -1:
        print("The binary tree array is full.")
        return
    inp = int(input("Enter the number to add: "))
    if root == -1:
        root = free
        arr[root][1] = inp
        free += 1
        return arr, root, free
    current = root
    while True:
        if inp > arr[current][1]:
            if arr[current][2] == 0:
                arr[current][2] = free
                arr[free][1] = inp
                break
            else:
                current = arr[current][2]
        elif inp < arr[current][1]:
            if arr[current][0] == 0:
                arr[current][0] = free
                arr[free][1] = inp
                break
            else:
                current = arr[current][0]
    free += 1
    if free == 20: free = -1
    return arr, root, free

def PrintAll(arr):
    for i in range(len(arr)):
        print(str(arr[i][0]) + " " + str(arr[i][1]) + " " + str(arr[i][2]))

def InOrder(arr, pointer):
    if arr[pointer][0] != 0:
        InOrder(arr, arr[pointer][0])
    print(arr[pointer][1])
    if arr[pointer][2] != 0:
        InOrder(arr, arr[pointer][2])

def main():
    ArrayNodes = [[0 for _ in range(3)] for _ in range(20)] #2D array of integers
    RootPointer = -1 #integer
    FreeNode = 0 #integer
    for i in range(10):
        ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)
    PrintAll(ArrayNodes)
    InOrder(ArrayNodes, RootPointer)

if __name__ == "__main__":
    main()
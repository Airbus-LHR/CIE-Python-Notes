global ArrayNodes
ArrayNodes = [[-1 for _ in range(2)] for _ in range(19)]
global FreeNode, RootPointer
FreeNode = 6
RootPointer = 0

def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    
def PostOrder(n):
    global ArrayNodes
    if ArrayNodes[n][0] != -1:
        PostOrder(ArrayNodes[n][0])
    if ArrayNodes[n][2] != -1:
        PostOrder(ArrayNodes[n][2])
    print(ArrayNodes[n][1])

def main():
    global ArrayNodes
    ArrayNodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]
    idx = SearchValue(RootPointer, 15)
    if idx != -1:
        print("Value found at index:", idx)
    else:
        print("Value not found.")
    print("Post-order traversal of the tree:")
    PostOrder(RootPointer)

if __name__ == "__main__":
    main()
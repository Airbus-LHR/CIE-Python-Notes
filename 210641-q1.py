class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

def outputNodes(startPointer, linkedList):
    idx = startPointer
    while idx != -1:
        print(linkedList[idx].data)
        idx = linkedList[idx].nextNode

def addNode(linkedList, startPointer, emptyList):
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        linkedList[emptyList] = node(int(input("Enter number to be added: ")), -1)
        idx = startPointer
        while True:
            if linkedList[idx].nextNode == -1:
                break
            idx = linkedList[idx].nextNode
        linkedList[idx].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        return True

def main():
    linkedList = [None] * 10
    startPointer = 0
    emptyList = 5
    linkedList[0] = node(1, 1)
    linkedList[1] = node(5, 4)
    linkedList[2] = node(6, 7)
    linkedList[3] = node(7, -1)
    linkedList[4] = node(2, 2)
    linkedList[5] = node(0, 6)  
    linkedList[6] = node(0, 8)
    linkedList[7] = node(56, 3)
    linkedList[8] = node(0, 9)
    linkedList[9] = node(0, -1)
    outputNodes(startPointer, linkedList)
    if addNode(linkedList, startPointer, emptyList):
        print("Sucessfully added")
    else:
        print("Failed to add.")
    outputNodes(startPointer, linkedList)

if __name__ == "__main__":
    main()
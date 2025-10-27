global LinkedList, FirstEmpty, FirstNode
LinkedList = [[-1, j + 1] for j in range(20)]
LinkedList[19][1] = -1
FirstEmpty = 0
FirstNode = -1
def InsertData():
    global LinkedList, FirstEmpty, FirstNode
    for i in range(5):
        a = int(input())
        if FirstEmpty > 19 or FirstEmpty < 0:
            return
        LinkedList[FirstEmpty][0] = a
        tmp = LinkedList[FirstEmpty][1]
        LinkedList[FirstEmpty][1] = FirstNode
        FirstNode = FirstEmpty
        FirstEmpty = tmp

def RemoveData(num):
    global FirstEmpty, LinkedList, FirstNode
    idx = FirstNode
    tmp = idx
    while idx != -1:
        if LinkedList[idx][0] == num:
            LinkedList[idx][0] = -1
            if idx == FirstNode: FirstNode = LinkedList[idx][1]
            LinkedList[tmp][1] = LinkedList[idx][1]
            LinkedList[idx][1] = FirstEmpty
            FirstEmpty = idx
        else:
            tmp = idx
            idx = LinkedList[idx][1]

def OutputLinkedList():
    global LinkedList, FirstNode
    idx = FirstNode
    while idx != -1:
        print(LinkedList[idx][0])
        idx = LinkedList[idx][1]

def main():
    global LinkedList, FirstEmpty, FirstNode
    InsertData()
    OutputLinkedList()
    RemoveData(5)
    print("After")
    OutputLinkedList()

if __name__ == "__main__":
    main()
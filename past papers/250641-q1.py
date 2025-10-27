global HeadPointer, TailPointer, NumberItems, Queue
Queue = [-1] * 20
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(item):
    global HeadPointer, TailPointer, NumberItems, Queue
    if NumberItems >= 20:
        return False
    if NumberItems == 0:
        HeadPointer = 0
    TailPointer += 1
    Queue[TailPointer] = item
    NumberItems += 1
    if NumberItems < 20:
        return True
    else: return False

def Dequeue():
    global HeadPointer, NumberItems, Queue
    if NumberItems == 0:
        return -1
    res = Queue[HeadPointer]
    NumberItems -= 1
    HeadPointer += 1
    return res

def main():
    for i in range(1, 26):
        if Enqueue(i):
            print(f"{i} Successful.")
        else: print(f"{i} Unsuccessful.")
    print(Dequeue())
    print(Dequeue())

if __name__ == "__main__":
    main()
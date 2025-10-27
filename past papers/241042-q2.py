class Queue:
    def __init__(self, arr, head, tail):
        self.QueueArray = arr #array of integer
        self.Headpointer = head #integer
        self.Tailpointer = tail #integer

def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer += 1
        return 1
    elif AQueue.Tailpointer > 99:
        return -1
    else:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Tailpointer += 1
        return 1
    
def Dequeue(AQueue):
    if AQueue.Headpointer == AQueue.Tailpointer:
        return -1
    res = AQueue.QueueArray[AQueue.Headpointer]
    AQueue.Headpointer += 1
    return res

def ReturnAllData(AQueue):
    res = ""
    for i in range(AQueue.Headpointer, AQueue.Tailpointer):
        res += str(AQueue.QueueArray[i]) + " "
    return res[:len(res) - 1]

def main():
    TheQueue = Queue([-1] * 100, -1, 0)
    for i in range(10):
        a = -1
        while a < 0:
            a = int(input("Enter the number to be added: "))
            if a < 0: print("The number must be greater than 0!")
        if Enqueue(TheQueue, a) == -1:
            print("Queue is full!")
            break
    print(ReturnAllData(TheQueue))
    for i in range(2):
        a = Dequeue(TheQueue)
        if a == -1:
            print("The queue is full")
        else:
            print(a)

if __name__ == "__main__":
    main()
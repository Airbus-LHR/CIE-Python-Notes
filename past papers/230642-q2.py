class SaleData:
    def __init__(self, ids, quantity):
        self.id = ids
        self.quantity = quantity

global CircularQueue
CircularQueue = [SaleData("", -1)] * 5
global Head, Tail, NumberOfItems
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(x):
    global CircularQueue, Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = x
        Tail += 1
        if Tail >= 5:
            Tail = 0
        NumberOfItems += 1
        return 1

def Dequeue():
    global CircularQueue, Head, NumberOfItems
    if NumberOfItems == 0:
        return None
    else:
        tmp = CircularQueue[Head]
        CircularQueue[Head] = SaleData("", -1)
        Head += 1
        NumberOfItems -= 1
        return tmp

def EnterRecord(ids, q):
    if Enqueue(SaleData(ids, q)) == 1:
        print("Stored")
    else:
        print("Full")

def main():
    global CircularQueue
    for i in range(6):
        EnterRecord(input("Please enter ID: "), input("Please enter quantity: "))
    t = Dequeue()
    if t == None:
        print("Empty!")
    else:
        print(f"ID: {t.id} Quantity: {t.quantity}")
    EnterRecord(input("Please enter ID: "), input("Please enter quantity: "))
    for i in range(len(CircularQueue)):
        print(f"ID: {CircularQueue[i].id} Quantity: {CircularQueue[i].quantity}")

if __name__ == "__main__":
    main()

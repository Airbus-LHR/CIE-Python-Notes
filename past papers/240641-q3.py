global QueueData, QueueHead, QueueTail
QueueHead = -1
QueueTail = -1
QueueData = [""] * 20

def Enqueue(item):
    global QueueData, QueueHead, QueueTail
    if QueueTail >= 19:
        return False
    else:
        QueueTail += 1
        QueueData[QueueTail] = item
        return True
    
def Dequeue():
    global QueueData, QueueHead, QueueTail
    if QueueTail == QueueHead:
        return "false"
    else:
        tmp = QueueData[QueueHead]
        QueueHead += 1
        return tmp

def StoreItems():
    cnt = 10
    for i in range(10):
        n = input("Enter a 7-character string: ")
        c = n[6]
        if c == "X": c = "10"
        t = int(n[:6])
        sum = 0
        while t != 0:
            sum += t % 10 * 3
            t //= 10
            sum += t % 10
            t //= 10
        if sum // 10 == int(c):
            cnt -= 1
            Enqueue(n[:6])
    print(f"There were {cnt} invalid items.")

def main():
    global QueueData, QueueHead, QueueTail
    QueueHead = 0
    StoreItems()
    a = Dequeue()
    if a == "false":
        print("The queue is empty.")
    else:
        print(a)

if __name__ == "__main__":
    main()
head = 0 #integer
tail = 0 #integer
size = 0 #integer
arr = [""] * 10 #array

def Enqueue(QueueArray, DataToAdd):
    global tail, size
    if size == 10:
        return False
    QueueArray[tail] = DataToAdd
    if tail >= 9:
        tail = 0
    else:
        tail += 1
    size += 1
    return True

def Dequeue():
    global head, size
    if size == 0:
        return False
    result = arr[head]
    arr[head] = None
    if head >= 9:
        head = 0
    else:
        head += 1
    size -= 1
    return result

def main():
    for i in range(11):
        a = input("Enter item to add: ")
        if (Enqueue(arr, a)):
            print("Item added")
        else:
            print("Queue full")
    print(Dequeue())
    print(Dequeue())

if (__name__ == "__main__"):
    main()
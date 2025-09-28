global Queue
Queue = [""] * 50
global HeadPointer
HeadPointer = -1
global TailPointer
TailPointer = 0
global Records
Records = [None] * 50 #array of RecordData
global NumberRecords
NumberRecords = 0 #integer

class RecordData:
    def __init__(self, ids, total):
        self.ID = ids #string
        self.Total = total #integer

def Enqueue(s):
    global TailPointer, HeadPointer
    if TailPointer - HeadPointer > 50:
        print("The queue is full.")
        return
    if Queue[0] == "":
        HeadPointer = 0
    Queue[TailPointer] = s
    TailPointer += 1
    return

def Dequeue():
    global TailPointer, HeadPointer
    if TailPointer == HeadPointer:
        print("The queue is empty.")
        return "Empty"
    tmp = Queue[HeadPointer]
    Queue[HeadPointer] = ""
    HeadPointer += 1
    return tmp

def ReadData():
    try:
        with open("QueueData.txt", encoding = 'utf-8') as f:
            for line in f:
                Enqueue(line.strip())
    except IOError:
        print("File not found.")

def TotalData():
    global NumberRecords, Records
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords] = RecordData(DataAccessed, 1)
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
    if Flag == False:
        Records[NumberRecords] = RecordData(DataAccessed, 1)
        NumberRecords += 1

def OutputRecords():
    global Records
    i = 0
    while Records[i] != None:
        print(f"ID {Records[i].ID} Total {Records[i].Total}")
        i += 1

def main():
    global TailPointer, HeadPointer, Records
    ReadData()
    for i in range(TailPointer - HeadPointer):
        TotalData()
    OutputRecords()

if __name__ == "__main__":
    main()

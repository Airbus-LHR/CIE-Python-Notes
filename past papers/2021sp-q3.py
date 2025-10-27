global QueueData, start, end
QueueData = [""] * 20
start = 0
end = -1
def Enqueue(item):
    global QueueData, start, end
    end += 1
    if end >= 20:
        return False
    else:
        QueueData[end] = item
        return True

def ReadFile():
    file = input("Enter file name: ")
    try:
        with open(file, "r", encoding = "utf-8") as f:
            for line in f:
                if not Enqueue(line.strip()): return 1
        return 2
    except IOError:
        return -1

def Remove():
    global QueueData, start, end
    res = ""
    for i in range(2):
        if end == start:
            return "No Items"
        else:
            res += QueueData[start] + " "
            start += 1
    return res[:len(res) - 1]

def main():
    c = ReadFile()
    if c == 2:
        print("Successfully added!")
    elif c == 1:
        print("Partially added as queue is full.")
    elif c == -1:
        print("File does not exist!")
if __name__ == "__main__":
    main()
global DataArray
DataArray = [0] * 100

def ReadFile():
    global DataArray
    try:
        with open("IntegerData.txt", "r", encoding = "utf-8") as f:
            i = 0
            for line in f:
                DataArray[i] = (int(line.strip()))
                i += 1
    except FileNotFoundError:
        print("File not found.")

def FindValues():
    global DataArray
    a = int(input("Enter a number between 1 and 100 inclusive: "))
    cnt = 0
    for i in range(len(DataArray)):
        if DataArray[i] == a:
            cnt += 1
    return cnt

def BubbleSort():
    global DataArray
    flag = False
    while not flag:
        flag = True
        for i in range(len(DataArray) - 1):
            if DataArray[i] > DataArray[i + 1]:
                DataArray[i], DataArray[i + 1] = DataArray[i + 1], DataArray[i]
                flag = False

def main():
    ReadFile()
    count = FindValues()
    print("The number of occurrences is:", count)
    BubbleSort()
    print("The sorted data is:")
    print(DataArray)

if __name__ == "__main__":
    main()
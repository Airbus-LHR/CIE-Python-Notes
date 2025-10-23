global DataStored, NumberItems
DataStored = [] #array of 20 items
NumberItems = 0 #integer

def Initialize():
    n = -1
    while(n < 1 or n > 20):
        n = int(input("Enter how many numbers to enter, between 1 and 20 inclusive: "))
    for i in range(n):
        DataStored.append(int(input()))

def BubbleSort():
    global DataStored
    flag = False
    while not flag:
        flag = True
        for i in range(len(DataStored) - 1):
            if DataStored[i] > DataStored[i + 1]:
                flag = False
                DataStored[i], DataStored[i + 1] = DataStored[i + 1], DataStored[i]

def BinarySearch(DataToFind):
    global DataStored
    left = 0
    right = len(DataStored) - 1
    while (right > left + 1):
        if DataStored[(left + right) // 2] == DataToFind:
            return (left + right) // 2
        elif DataStored[(left + right) // 2] > DataToFind:
            right = (left + right) // 2
        else:
            left = (left + right) // 2
    return -1

def main():
    global NumberItems, DataStored
    Initialize()
    for i in range(len(DataStored)):
        print(DataStored[i])
    BubbleSort()
    for i in range(len(DataStored)):
        print(DataStored[i])
    print(BinarySearch(int(input("Enter the number to find: "))))

if __name__ == "__main__":
    main()
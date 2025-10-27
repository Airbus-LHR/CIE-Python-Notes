def InsertionSort(TheData):
    for count in range(len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1

def OutputArray(arr):
    for i in arr:
        print(i, end = " ")

def Find(arr, n):
    for i in arr:
        if i == n:
            print("found")
            return True
    print("not found")
    return False

def main():
    TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
    print("Before")
    OutputArray(TheData)
    print("\nAfter")
    InsertionSort(TheData)
    OutputArray(TheData)
    print()
    Find(TheData, int(input("Enter number to find: ")))
    Find(TheData, int(input("Enter number to find: ")))

if __name__ == "__main__":
    main()
global arrayData 
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(x):
    for i in range(len(arrayData)):
        if arrayData[i] == x:
            return True
    return False

def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] < arrayData[y + 1]:
                arrayData[y], arrayData[y + 1] = arrayData[y + 1], arrayData[y]

def main():
    if (linearSearch(int(input("Enter an integer: ")))):
        print("Integer found!")
    else:
        print("Intger not found.")
    bubbleSort()
    for i in range(len(arrayData)):
        print(arrayData[i])

if __name__ == "__main__":
    main()
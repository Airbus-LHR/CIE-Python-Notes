def ReadData():
    arr = []
    try:
        with open("Data(2).txt", "r", encoding = "utf-8") as f:
            for line in f:
                arr.append(line.strip())
        return arr
    except FileNotFoundError:
        print("File does not exist.")

def FormatArray(arr):
    res = ""
    for i in range(len(arr)):
        res += arr[i] + " "
    print(res[:len(res) - 1])

def CompareStrings(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return 2
        elif b[i] > a[i]:
            return 1
        
def Bubble(arr):
    flag = False
    while not flag:
        flag = True
        for i in range(len(arr) - 1):
            if CompareStrings(arr[i], arr[i + 1]) == 2:
                flag = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def main():
    a = ReadData()
    Bubble(a)
    FormatArray(a)

if __name__ == "__main__":
    main()
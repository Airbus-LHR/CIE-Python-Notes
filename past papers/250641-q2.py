def ReadData():
    file = input("Enter file name: ")
    try:
        arr = []
        with open(file, "r", encoding = "utf-8") as f:
            for line in f:
                arr.append(line.strip())
        return arr
    except IOError:
        print("File does not exist.")

def StoreData(DataToStore, file):
    try:
        with open(file, "w") as f:
            for i in DataToStore:
                f.write(str(i) + "\n")
    except:
        print("Cannot write lines to file")

def SplitData(DataArray):
    red = []
    green = []
    blue = []
    orange = []
    yellow = []
    pink = []
    for i in DataArray:
        if "red" in i:
            red.append(int(i[:i.index(",")]))
        elif "green" in i:
            green.append(int(i[:i.index(",")]))
        elif "blue" in i:
            blue.append(int(i[:i.index(",")]))
        elif "orange" in i:
            orange.append(int(i[:i.index(",")]))
        elif "yellow" in i:
            yellow.append(int(i[:i.index(",")]))
        else:
            pink.append(int(i[:i.index(",")]))
    StoreData(red, "Red.txt")
    StoreData(green, "Green.txt")
    StoreData(blue, "Blue.txt")
    StoreData(orange, "Orange.txt")
    StoreData(yellow, "yellow.txt")
    StoreData(pink, "pink.txt")

def main():
    arr = ReadData()
    SplitData(arr)

if __name__ == "__main__":
    main()
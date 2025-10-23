class Tree:
    def __init__(self, tn, hg, mh, mw, eg):
        self.__TreeName = tn #string
        self.__HeightGrowth = hg #integer
        self.__MaxHeight = mh #integer
        self.__MaxWidth = mw #integer
        self.__EverGreen = eg #string
    def GetTreeName(self):
        return self.__TreeName
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEvergreen(self):
        return self.__EverGreen

def ReadData():
    arr = [] #array of type Tree
    try:
        with open("Trees.txt", "r", encoding = "utf-8") as f:
            for line in f:
                lst = line.split(",")
                arr.append(Tree(lst[0].strip(), int(lst[1]), int(lst[2]), int(lst[3]), lst[4].strip()))
        return arr
    except FileNotFoundError:
        print("File does not exist!")

def PrintTrees(a):
    print(f"{a.GetTreeName()} has a maximum height {a.GetMaxHeight()} a maximum width {a.GetMaxWidth()} and grows {a.GetGrowth()} cm a year.", end = " ")
    if a.GetEvergreen() == "Yes":
        print("It does not lose its leaves.")
    else:
        print("It loses its leaves each year.")

def ChooseTree(arr):
    h = int(input("Enter maximum height required: "))
    w = int(input("Enter maximum width required: "))
    e = input("Enter wheter evergreen or not, yes or no: ")
    global res
    res = []
    for i in range(len(arr)):
        if arr[i].GetMaxHeight() <= h and arr[i].GetMaxWidth() <= w and arr[i].GetEvergreen().casefold() == e.casefold():
            res.append(arr[i])
    print(len(res))
    if len(res) == 0:
        print("No trees meet the requirement.")
    else:
        for i in range(len(res)):
            PrintTrees(res[i])
        name = input("Enter the name of the tree you want to buy: ")
        height = int(input("Enter the height of the tree when you bought: "))
        for i in range(len(res)):
            if res[i].GetTreeName().casefold() == name.casefold():
                print(f"The tree will take {(res[i].GetMaxHeight() - height) / res[i].GetGrowth()} years to reach its maximum height of {res[i].GetMaxHeight()} cm.")

def main():
    arr = ReadData()
    PrintTrees(arr[0])
    ChooseTree(arr)

if __name__ == "__main__":
    main()
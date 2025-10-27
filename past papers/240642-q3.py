def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    RecursiveInsertion(IntegerArray, NumberElements - 1)
    LastItem = IntegerArray[NumberElements - 1]
    CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] <= LastItem:
            LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray):
    sorted = 0
    idx = 0
    while sorted < len(IntegerArray):
        min = IntegerArray[sorted]
        for i in range(sorted, len(IntegerArray)):
            if IntegerArray[i] < min:
                idx = i
                min = IntegerArray[i]
        j = idx
        while j > sorted:
            IntegerArray[j], IntegerArray[j - 1] = IntegerArray[j - 1], IntegerArray[j]
            j -= 1
        sorted += 1
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):
    if Last < First:
        return -1
    elif IntegerArray[(First + Last) // 2] == ToFind:
        return (First + Last + 1) // 2
    elif IntegerArray[(First + Last) // 2] > ToFind:
        return BinarySearch(IntegerArray, First, (First + Last - 1) // 2, ToFind)
    else:
        return BinarySearch(IntegerArray, (First + Last + 1) // 2, Last, ToFind)

def main():
    NumberArray = [100, 85, 644, 22, 15, 8, 1]
    print("Iterative")
    res = IterativeInsertion(NumberArray)
    for i in range(len(res)):
        print(res[i], end = " ")
    idx = BinarySearch(NumberArray, 0, len(NumberArray) - 1, 644)
    if idx == -1:
        print("\nNot found.")
    else:
        print(f"\n{idx}")

if __name__ == "__main__":
    main()
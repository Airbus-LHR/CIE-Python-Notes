StackData = [0] * 10
StackPointer = 0

def iterate():
    global StackData, StackPointer
    for i in range(10):
        print(StackData[i])
    print("Stack Pointer:", StackPointer)

def push(value):
    global StackData, StackPointer
    if StackPointer < 10:
        StackData[StackPointer] = value
        StackPointer += 1
        return True
    else:
        return False

def pop():
    global StackData, StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer -= 1
        return StackData[StackPointer]

def main():
    global StackData, StackPointer
    for i in range(11):
        inp = int(input("Enter a number to push onto the stack: "))
        if not push(inp):
            print("Stack Overflow")
        else:
            print("Item Added")
    iterate()
    pop()
    pop()
    iterate()

if __name__ == "__main__":
    main()
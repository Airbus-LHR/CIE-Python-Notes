import random
def iterate(arr):
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end=' ')
        print()

def binarysearch(arr, lower, upper, value):
    if upper > lower:
        mid = (lower + upper - 1) // 2
        if arr[0][mid] == value:
            return mid
        elif arr[0][mid] > value:
            return binarysearch(arr, lower, mid - 1, value)
        else:
            return binarysearch(arr, mid + 1, upper, value)
    return -1

def main():
    rows = 10
    cols = 10
    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(10):
        for j in range(10):
            arr[i][j] = random.randint(1, 100)
    iterate(arr)
    arraylength = 10
    for x in range(arraylength):
        for y in range(arraylength - 1):
            for z in range(arraylength - y - 1):
                if (arr[x][z] > arr[x][z + 1]):
                    tmp = arr[x][z]
                    arr[x][z] = arr[x][z + 1]
                    arr[x][z + 1] = tmp
    print()
    iterate(arr)
    for i in range(2):    
        value = int(input("Enter a number to search: "))
        print(binarysearch(arr, 0, arraylength - 1, value))

if __name__ == "__main__":
    main()
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def RecursiveBinarySearch(arr, l, r, target):
    if r < l:
        print(1)
        return -1
    mid = (l + r) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return RecursiveBinarySearch(arr, l, mid - 1, target)
    else:
        return RecursiveBinarySearch(arr, mid + 1, r, target)
    
def IterativeBinarySearch(arr, target):
    l = 0
    r = len(arr) - 1
    while(r >= l):
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

for i in range(len(arr)):
    print(f"Recursive found {arr[i]} at position {RecursiveBinarySearch(arr, 0, len(arr) - 1, arr[i])}")
    print(f"Iterative found {arr[i]} at position {IterativeBinarySearch(arr, arr[i])}")
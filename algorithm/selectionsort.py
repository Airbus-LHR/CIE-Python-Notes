import random
def SelectionSort(arr):
    sorted = 0
    idx = 0
    while sorted < len(arr) - 1:
        min = arr[sorted]
        idx = sorted
        for i in range(sorted, len(arr)):
            if arr[i] < min:
                idx = i
                min = arr[i]
        arr[idx], arr[sorted] = arr[sorted], arr[idx]
        sorted += 1
    return arr

arr = []
for i in range(10):
    arr.append(random.randint(0, 100))
print(arr)
SelectionSort(arr)
print(arr)
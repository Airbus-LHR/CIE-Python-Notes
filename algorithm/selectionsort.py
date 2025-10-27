import random
def SelectionSort(arr):
    sorted = 0
    idx = 0
    while sorted < len(arr):
        min = arr[sorted]
        for i in range(sorted, len(arr)):
            if arr[i] < min:
                idx = i
                min = arr[i]
        j = idx
        while j > sorted:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        sorted += 1
    return arr

arr = []
for i in range(10):
    arr.append(random.randint(0, 100))
print(arr)
SelectionSort(arr)
print(arr)
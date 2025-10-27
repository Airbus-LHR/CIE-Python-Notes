import random
def BubbleSort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

arr = []
for i in range(10):
    arr.append(random.randint(0, 100))
print(arr)
BubbleSort(arr)
print(arr)
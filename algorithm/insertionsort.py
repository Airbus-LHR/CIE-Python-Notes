import random
def InsertionSort(arr):
    sorted = 0
    while sorted < len(arr):
        if sorted > 0:
            m = sorted
            ins = arr[m]
            while ins < arr[m - 1] and m > 0:
                arr[m], arr[m - 1] = arr[m - 1], arr[m]
                m -= 1
        sorted += 1
    return arr

arr = []
for i in range(10):
    arr.append(random.randint(0, 100))
print(arr)
InsertionSort(arr)
print(arr)
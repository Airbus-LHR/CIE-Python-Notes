def PrintArray(arr):
    for item in arr:
        print(item, end=' ')

def LinearSearch(arr, target):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == target:
            cnt += 1
    return cnt

def main():
    DataArray = []
    with open("Data.txt", "r", encoding = "utf-8") as f:
        for line in f:
            DataArray.append(int(line.strip()))
    target = int(input("Enter the target number between 0 and 100 inclusive: "))
    count = LinearSearch(DataArray, target)
    print(f"The number {target} is found {count} times.")

if __name__ == "__main__":
    main()
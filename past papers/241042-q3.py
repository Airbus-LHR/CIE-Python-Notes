def ReadData():
    res = [["" for i in range(3)] for j in range(7)]
    try:
        with open("HighScoreTable.txt", "r", encoding = "utf-8") as f:
            i = 0
            while True:
                if i >= len(res):
                    break
                res[i][0] = f.readline().strip()
                res[i][1] = f.readline().strip()
                res[i][2] = f.readline().strip()
                if res[i][0] == "":
                    break
                i += 1
            return res
    except IOError:
        print("File does not exist")

def SortScore(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i][1] < arr[i + 1][1] or arr[i][1] == arr[i + 1][1] and arr[i][2] < arr[i + 1][2]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def OutputHighScores(arr):
    for i in arr:
        print(f"{i[0]} reach level {i[1]} with a score of {i[2]}.")

def main():
    HighScores = [["" for i in range(3)] for j in range(7)]
    HighScores = ReadData()
    print("Before")
    OutputHighScores(HighScores)
    SortScore(HighScores)
    print("After")
    OutputHighScores(HighScores)

if __name__ == "__main__":
    main()
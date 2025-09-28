score = []
name = []
newname = []
newscore = []
def ReadHighScores():
    i = 0
    with open(r"C:\Users\Sunny\Downloads\HighScore.txt", "r", encoding="utf-8") as f:
        for line in f:
            if (i % 2 == 0):
                name.append(line)
            else:
                score.append(line)
            i += 1
def OutputHighScores():
    for i in range(0, 10):
        print(name[i].strip() + " " + score[i].strip())

def updateScore(n, s):
    j = 0
    while(j < 9):
        if (s < int(score[j])):
            j += 1
        else:
            break
    if (s > int(score[j])):
        for k in range(0, 9):
            if (k == j):
                newname.append(n)
                newscore.append(str(s))
            newname.append(name[k].strip())
            newscore.append(score[k].strip())
    else:
        for i in range(0, 10):
            newname.append(name[i].strip())
            newscore.append(score[i].strip())
    for i in range(0, 10):
        print(newname[i] + " " + newscore[i])
    
def WriteTopTen():
    with open(r"C:\Users\Sunny\Downloads\output.txt", "w", encoding="utf-8") as f:
        for i in range(0, 10):
            f.write(newname[i] + "\n")
            f.write(newscore[i] + "\n")
    
def main():
    n = input("Enter a 3-character player name: ")
    s = int(input("Enter score between 1 and 100000 inclusive: "))
    ReadHighScores()
    OutputHighScores()
    print()
    updateScore(n, s)
    WriteTopTen()
    
if (__name__ == "__main__"):
    main()
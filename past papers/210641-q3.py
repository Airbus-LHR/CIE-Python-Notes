class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question #string
        self.__answer = answer #string
        self.__points = points #integer
    def getQuestion(self):
        return self.__question
    def checkAnswer(self, ans):
        return ans == self.__answer
    def getPoints(self, n):
        if n == 1:
            return self.__points
        elif n == 2:
            return self.__points // 2
        elif n == 3 or n == 4:
            return self.__points // 4
        else:
            return 0

arrayTreasure = [None]

def readData():
    global arrayTreasure
    try:
        with open("TreasureChestData.txt", encoding='utf-8') as f:
            for i in range(5):
                arrayTreasure.append(TreasureChest(f.readline().strip(), f.readline().strip(), int(f.readline().strip())))
    except FileNotFoundError:
        print("File not found.")

def main():
    readData()
    num = int(input("Enter a question number between 1~5: "))
    print(arrayTreasure[num].getQuestion())
    cnt = 0
    while True:
        cnt += 1
        if arrayTreasure[num].checkAnswer(input()):
            break
        else: print("Try again:", end="")
    print("You earned " + str(arrayTreasure[num].getPoints(cnt)) + " points!")

if __name__ == "__main__":
    main()
class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour
        self.selected = False
    def getNumber(self):
        return self.__Number
    def getColour(self):
        return self.__Colour

card = [None] * 30
def ChooseCard(idx):
    if idx <= 0 or idx > 30:
        return -1
    elif card[idx - 1].selected:
        return -1
    else:
        card[idx - 1].selected = True
        return idx - 1

def main():
    global card
    Player1 = [None] * 4
    with open("CardValues.txt", "r", encoding = 'utf-8') as f:
        for i in range(30):
            num = f.readline().strip()
            name = f.readline().strip()
            card[i] = Card(int(num), name)
    for i in range(4):
        idx = int(input("Player 1, choose your card (1-30): "))
        chosen = ChooseCard(idx)
        while chosen == -1:
            print("Invalid choice or card already selected. Please choose again.")
            idx = int(input("Player 1, choose your card (1-30): "))
            chosen = ChooseCard(idx)
        Player1[i] = card[chosen]
    for i in range(4):
        print("Card number:", Player1[i].getNumber(), "Card Colour:", Player1[i].getColour())

if __name__ == "__main__":
    main()
class Card:
    def __init__(self, n, c):
        self.__Number = n #integer
        self.__Colour = c #string
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

class Hand:
    def __init__(self, a, b, c, d, e):
        self.__Cards = [a, b, c, d, e] #list of Card objects
        self.__FirstCard = 0
        self.__NumberCards = 5
    def GetCard(self, i):
        return self.__Cards[i]

def CalculateValue(p):
    score = 0
    for i in range(5):
        if p.GetCard(i).GetColour() == "red":
            score += 5
        elif p.GetCard(i).GetColour() == "blue":
            score += 10
        elif p.GetCard(i).GetColour() == "yellow":
            score += 15
    return score

def main():
    card1 = Card(1, "red")
    card2 = Card(2, "red")
    card3 = Card(3, "red")
    card4 = Card(4, "red")
    card5 = Card(5, "red")

    card6 = Card(1, "blue")
    card7 = Card(2, "blue")
    card8 = Card(3, "blue")
    card9 = Card(4, "blue")
    card10 = Card(5, "blue")

    card11 = Card(1, "yellow")
    card12 = Card(2, "yellow")
    card13 = Card(3, "yellow")
    card14 = Card(4, "yellow")
    card15 = Card(5, "yellow")

    player1 = Hand(card1, card2, card3, card4, card11)
    player2 = Hand(card12, card13, card14, card15, card6)
    if CalculateValue(player1) > CalculateValue(player2):
        print("Player 1 wins")
    else:
        print("Player 2 wins")

if __name__ == "__main__":
    main()
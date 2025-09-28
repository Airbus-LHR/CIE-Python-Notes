class Balloon:
    def __init__(self, color, defence):
        self.__health = 100 #integer
        self.__colour = color #string
        self.__defence = defence #string
    def GetDefenceItem(self):
        return self.__defence
    def ChangeHealth(self, change):
        self.__health += change
    def CheckHealth(self):
        return self.__health <= 0

def Defend(balloon):
    s = int(input("Enter strength of opponent: "))
    balloon.ChangeHealth(-s)
    print(balloon.GetDefenceItem())
    if (balloon.CheckHealth()):
        print("It has no health remaining")
    else:
        print("It has health remaining")
    return balloon

def main():
    d = input("Enter defence item: ")
    c = input("Enter colour: ")
    Balloon1 = Balloon(c, d)
    Defend(Balloon1)

if (__name__ == "__main__"):
    main()
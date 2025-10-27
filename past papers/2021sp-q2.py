from datetime import date
class HiddenBox:
    # __BoxName string
    # __Creator string
    # __DateHidden date
    # __GameLocation string
    # __LastFinds 2D array
    # __Active boolean
    def __init__(self, name, creator, date, location):
        self.__BoxName = name
        self.__Creator = creator
        self.__DateHidden = date
        self.__GameLocation = location
        self.__Active = False
        self.__LastFinds = [["" for i in range(2)] for j in range(10)]
    def GetBoxName(self):
        return self.__BoxName
    def GetGameLocation(self):
        return self.__GameLocation
    
class PuzzleBox(HiddenBox):
    def __init__(self, name, creator, date, location, puzzle, solution):
        super().__init__(name, creator, date, location)
        self.__PuzzleText = puzzle
        self.__Solution = solution

def NewBox(arr):
    name = input("Enter the name of the box: ")
    creator = input("Enter the creator: ")
    day = int(input("Enter the date day: "))
    month = int(input("Enter the date month: "))
    year = int(input("Enter the date yaer: "))
    d = date(year, month, day)
    location = input("Enter location: ")
    arr.append(HiddenBox(name, creator, d, location))

def main():
    TheBoxes = []
    NewBox(TheBoxes)

if __name__ == "__main__":
    main()
class Character:
    def __init__(self, name, x, y):
        self.Name = name
        self.XPosition = x
        self.YPosition = y
    def GetXPosition(self):
        return self.XPosition
    def GetYPosition(self):
        return self.YPosition
    def SetXPosition(self, x):
        self.XPosition = min(max(x,0), 10000)
    def SetYPosition(self, y):
        self.YPosition = min(max(y,0), 10000)
    def Move(self, s):
        if s.lower() in ['up', 'down', 'left', 'right']:
            if s == 'up':
                self.SetYPosition(self.GetYPosition() + 10)
            elif s == 'down':
                self.SetYPosition(self.GetYPosition() - 10)
            elif s == 'left':
                self.SetXPosition(self.GetXPosition() - 10)
            else:
                self.SetXPosition(self.GetXPosition() + 10)
        else: print("Should be left, right, up, or down.")

class BikeCharacter(Character):
    def __init__(self, name, x, y):
        Character.__init__(self, name, x, y)
    def Move(self, s):
        if s.lower() in ['up', 'down', 'left', 'right']:
            if s == 'up':
                self.SetYPosition(self.GetYPosition() + 20)
            elif s == 'down':
                self.SetYPosition(self.GetYPosition() - 20)
            elif s == 'left':
                self.SetXPosition(self.GetXPosition() - 20)
            else:
                self.SetXPosition(self.GetXPosition() + 20)
        else: print("Should be left, right, up, or down.")
        
def main():
    Jack = Character("Jack", 50, 50)
    Karla = BikeCharacter("Karla", 100, 50)
    n = ""
    while n.lower() not in ["jack", "karla"]:
        n = input("Which character to move? Jack or Karla: ")
    d = input("Which direction do you want to move: ")
    if n.lower() == "jack":
        Jack.Move(d)
        print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
    else:
        Karla.Move(d)
        print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")
        
if __name__ == "__main__":
    main()

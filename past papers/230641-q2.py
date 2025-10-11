class Vehicle:
    def __init__(self, ids, m, i):
        self.__ID = ids
        self.__MaxSpeed = m
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = i
        self.__HorizontalPosition = 0
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def SetCurrentSpeed(self, s):
        self.__CurrentSpeed = s
    def SetHorizontalPosition(self, p):
        self.__HorizontalPosition = p
    def IncreaseSpeed(self):
        self.SetCurrentSpeed(min(self.GetMaxSpeed(), self.GetCurrentSpeed() + self.GetIncreaseAmount()))
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())

class Helicopter(Vehicle):
    def __init__(self, ids, m, i, change, mh):
        super().__init__(ids, m, i)
        self.__VerticalPosition = 0
        self.__Change = change
        self.__MaxHeight = mh
    def GetVerticalPosition(self):
        return self.__VerticalPosition
    def IncreaseSpeed(self):
        self.__VerticalPosition = min(self.__VerticalPosition + self.__Change, self.__MaxHeight)
        self.SetCurrentSpeed(min(self.GetMaxSpeed(), self.GetIncreaseAmount() + self.GetCurrentSpeed()))
        self.SetHorizontalPosition( self.GetHorizontalPosition() + self.GetCurrentSpeed())

def printStatus(v):
    if type(v) == Vehicle:
        print(f"Vehicle {v._Vehicle__ID} is at horizontal position {v.GetHorizontalPosition()} with speed {v.GetCurrentSpeed()}.")
    elif type(v) == Helicopter:
        print(f"Helicopter {v._Vehicle__ID} is at horizontal position {v.GetHorizontalPosition()} with speed {v.GetCurrentSpeed()} and altitude {v.GetVerticalPosition()}.")
    else:
        print("Unknown vehicle type.")

def main():
    a = Vehicle("Tiger", 100, 20)
    b = Helicopter("Lion", 350, 40, 3, 100)
    a.IncreaseSpeed()
    a.IncreaseSpeed()
    printStatus(a)
    b.IncreaseSpeed()
    b.IncreaseSpeed()
    printStatus(b)

if __name__ == "__main__":
    main()
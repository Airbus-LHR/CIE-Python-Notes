class EventItem:
    def __init__(self, n, t, d):
        self.__EventName = n #string
        self.__Type = t #string
        self.__Difficulty = d #integer
    def GetName(self):
        return self.__EventName
    def GetDifficulty(self):
        return self.__Difficulty
    def GetEventType(self):
        return self.__Type

class Character:
    def __init__(self, j, s, r, d):
        self.__Jump = j #integer
        self.__Swim = s #integer
        self.__Run = r #integer
        self.__Drive = d #integer
    def CalculateScore(self, event, difficulty):
        if event.lower() == "jump":
            return min(100 - (difficulty - self.__Jump) * 20, 100)
        elif event.lower() == "swim":
            return min(100 - (difficulty - self.__Swim) * 20, 100)
        elif event.lower() == "run":
            return min(100 - (difficulty - self.__Run) * 20, 100)
        else:
            return min(100 - (difficulty - self.__Drive) * 20, 100)

def main():
    Group = [EventItem("Bridge", "jump", 3), EventItem("Water wade", "swim", 4), EventItem("100 mile run", "run", 5), EventItem("Gridlock", "drive", 2), EventItem("Wall on wall", "jump", 4)]
    Tarz = Character(5, 3, 5, 1)
    Geni = Character(2, 2, 3, 4)
    st = 0
    sg = 0
    for i in Group:
        a = Tarz.CalculateScore(i.GetName(), i.GetDifficulty())
        b = Geni.CalculateScore(i.GetName(), i.GetDifficulty())
        st += a
        sg += b
        if a > b:
            print(f"Tarz wins the event {i.GetName()}.")
        elif a < b:
            print(f"Geni wins the event {i.GetName()}.")
        else:
            print(f"The event {i.GetName()} is a draw.")
    if st > sg:
        print("Tarz has a higher score.")
    elif st < sg:
        print("Geni has a higher score.")
    else:
        print("The group is a draw")

if __name__ == "__main__":
    main()
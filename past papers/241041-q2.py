class Horse:
    def __init__(self, n, m, p):
        self.__Name = n #string
        self.__MaxFenceHeight = m #integer
        self.__PercentageSuccess = p #integer
    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    def Success(self, height, risk):
        if height > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2
        else:
            return self.__PercentageSuccess * (1 - 0.1 * (risk - 1))

class Fence:
    def __init__(self, h, r):
        self.__Height = h #integer
        self.__Risk = r #integer
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk

def main():
    Horses = [Horse("Beauty", 150, 72), Horse("Jet", 160, 65)]
    for i in Horses:
        print(i.GetName())
    Course = []
    h = 0
    r = 0
    for i in range(4):
        h = 0
        r = 0
        while h < 70 or h > 180 or r < 1 or r > 5:
            h = int(input("Enter height: "))
            r = int(input("Enter risk: "))
            if h < 70 or h > 180 or r < 1 or r > 5:
                print("Height must between 70 and 180 and Risk must between 1 and 5.")
        Course.append(Fence(h, r))
    for i in range(2):
        for j in range(4):
            print(f"The horse {Horses[i].GetName()} at fence {j + 1} has a {Horses[i].Success(Course[j].GetHeight(), Course[j].GetRisk())} % chance of success")
    for i in Horses:
        total = 0
        for j in Course:
            total += i.Success(j.GetHeight(), j.GetRisk())
        print(f"The horse {i.GetName()} has an average {total / len(Course)}% chance of jumping over all four fences.")

if __name__ == "__main__":
    main()
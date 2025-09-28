from datetime import date
class Character:
    def __init__(self, name, date, iq, speed):
        self.__CharacterName = name #string
        self.__DateOfBirth = date #date
        self.Intelligence = iq #float
        self.__Speed = speed #integer
    def GetIntelligence(self):
        return self.Intelligence
    def GetName(self):
        return self.__CharacterName
    def SetIntelligence(self, x):
        self.Intelligence = x
    def Learn(self):
        self.Intelligence *= 1.1
    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year

class MagicCharacter(Character):
    def __init__(self, name, date, iq, speed, element):
        Character.__init__(self, name, date, iq, speed)
        self.__Element = element
    def Learn(self):
        if self.__Element.lower() in ['fire', 'water']:
            self.Intelligence *= 1.2
        elif self.__Element.lower() == 'earth':
            self.Intelligence *= 1.3
        else:
            self.Intelligence *= 1.1

def main():
    FirstCharacter = Character("Royal", date(2019, 1, 1), 70.0, 30)
    FirstCharacter.Learn()
    print(f"Name: {FirstCharacter.GetName()}\nAge: {FirstCharacter.ReturnAge()}\nIntelligence: {FirstCharacter.GetIntelligence()}")
    FirstMagic = MagicCharacter("Light", date(2018, 3, 3), 75.0, 22, 'fire')
    FirstMagic.Learn()
    print(f"Name: {FirstMagic.GetName()}\nAge: {FirstMagic.ReturnAge()}\nIntelligence: {FirstMagic.GetIntelligence()}")

if __name__ == "__main__":
    main()

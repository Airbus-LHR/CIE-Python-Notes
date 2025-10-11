global Animal, AnimalTopPointer, Colour, ColourTopPointer
Animal = [""] * 20
AnimalTopPointer = 0
Colour = [''] * 10
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True
    
def PopAnimal():
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer -= 1
        return Animal[AnimalTopPointer]
    
def PushColour(DataToPush):
    global Colour, ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True
    
def PopColour():
    global Colour, ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer -= 1
        return Colour[ColourTopPointer]

def ReadData():
    try:
        with open("AnimalData.txt", "r", encoding = "utf-8") as f:
            for line in f:
                PushAnimal(line.strip())
    except FileNotFoundError:
        print("File not found.")
    try:
        with open("ColourData.txt", "r", encoding = "utf-8") as f:
            for line in f:
                PushColour(line.strip())
    except FileNotFoundError:
        print("File not found.")

def OutputItem():
    global Animal, AnimalTopPointer, Colour, ColourTopPointer
    a = PopAnimal()
    c = PopColour()
    if a == "":
        print("No animal.")
        PushAnimal(a)
    elif c == "":
        print("No colour.")
        PushColour(c)
    else:
        print(f"{c} {a}")

def main():
    ReadData()
    for i in range(4):
        OutputItem()

if __name__ == "__main__":
    main()
def IterativeVowels(Value):
    total = 0
    LengthString = len(Value)
    for x in range(LengthString):
        FirstCharacter = Value[0: 1]
        if FirstCharacter in ['a', 'e', 'i', 'o', 'u']:
            total += 1
        Value = Value[1:]
    return total

def RecursiveVowels(Value):
    LengthString = len(Value)
    if LengthString == 0:
        return 0
    for x in range(LengthString):
        FirstCharacter = Value[0: 1]
        if FirstCharacter in ['a', 'e', 'i', 'o', 'u']:
            return 1 + RecursiveVowels(Value[1:])
        else:
            return RecursiveVowels(Value[1:])

def main():
    print(RecursiveVowels("imagine"))

if __name__ == "__main__":
    main()

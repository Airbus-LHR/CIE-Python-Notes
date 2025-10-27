global NumberWords, WordArray
NumberWords = -1
WordArray = []
def ReadWords(file):
    global NumberWords, WordArray
    try:
        with open(file, "r", encoding = "utf-8") as f:
            for line in f:
                NumberWords += 1
                WordArray.append(line.strip())
        Play()
    except FileNotFoundError:
        print("File does not exist!")

def Play():
    global NumberWords, WordArray
    print(WordArray[0])
    cnt = 0
    while True:
        ans = input("Enter the word: ")
        if ans.lower() == "no":
            break
        elif ans in WordArray:
            cnt += 1
            for i in range(len(WordArray)):
                if WordArray[i] == ans.lower():
                    WordArray[i] = None
            print("Answer correct!")
        else:
            print("Answer incorrect!")
    print(f"You got {cnt / len(WordArray) * 100:.2f}% of answers correct!")
    if cnt != len(WordArray):
        print("Here are words you didn't answer:")
        for i in range(len(WordArray)):
            if WordArray[i] != None:
                print(WordArray[i])

def main():
    f = input("Enter file easy, medium, or hard: ")
    if f.lower() in ["easy", "medium", "hard"]: ReadWords(f"{f[0].upper() + f[1:].lower()}.txt")

if __name__ == "__main__":
    main()
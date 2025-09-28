global StackVowel, StackConsonant
StackVowel = [''] * 100 #array of char
StackConsonant = [''] * 100 #array of char
global VowelTop
VowelTop = 0 #integer
global ConsonantTop
ConsonantTop = 0 #integer

def PushData(x):
    global StackVowel, StackConsonant, VowelTop, ConsonantTop
    if x in ['a', 'e', 'i', 'o', 'u']:
        if VowelTop == 99:
            print("Stack vowel is full")
        else:
            StackVowel[VowelTop] = x
            VowelTop += 1
    else:
        if ConsonantTop == 99:
            print("Stack consonant is full")
        else:
            StackConsonant[ConsonantTop] = x
            ConsonantTop += 1

def ReadData():
    with open("StackData.txt", encoding = 'utf-8') as f:
        for line in f:
            PushData(line.strip())

def PopVowel():
    global StackVowel, VowelTop
    if VowelTop == 0:
        return "No data"
    else:
        VowelTop -= 1
        tmp = StackVowel[VowelTop]
        StackVowel[VowelTop] = ''
        return tmp

def PopConsonant():
    global StackConsonant, ConsonantTop
    if ConsonantTop == 0:
        return "No data"
    else:
        ConsonantTop -= 1
        tmp = StackConsonant[ConsonantTop]
        StackConsonant[ConsonantTop] = ''
        return tmp

def main():
    ReadData()
    cnt = 0
    res = ""
    while cnt < 5:
        a = input("Enter either vowel or consonant: ")
        if a.lower() == 'vowel':
            tmp = PopVowel()
        else:
            tmp = PopConsonant()
        if tmp != "No data":
            res += tmp
            cnt += 1
        else:
            print(f"The {a.lower()} stack is empty, choose the other one.")
    print(res)

if __name__ == "__main__":
    main()

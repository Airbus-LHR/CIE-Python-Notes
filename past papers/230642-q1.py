global Animals
Animals = [""] * 10

def SortDescending():
    global Animals
    ArrayLength = len(Animals)
    for x in range(0, ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                Animals[y], Animals[y + 1] = Animals[y + 1], Animals[y]

def main():
    global Animals
    Animals = ['horse','lion','rabbit','mouse','bird','deer','whale','elephant','kangaroo','tiger']
    SortDescending()
    for i in range(len(Animals)):
        print(Animals[i])

if __name__ == "__main__":
    main()

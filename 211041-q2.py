class Picture:
    def __init__(self, description, width, height, framecolor):
        self.__descriptiopn = description #string
        self.__width = width #integer
        self.__height = height #integer
        self.__framecolor = framecolor #string
    def getDescription(self):
        return self.__descriptiopn
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getFrameColor(self):
        return self.__framecolor
    def SetDescription(self, x):
        self.__descriptiopn = x

arr = [None] * 100

def ReadData():
    global arr
    cnt = 0
    try:
        with open("Pictures.txt", encoding='utf-8') as f:
            while True:
                try:
                    arr[cnt] = Picture(f.readline().strip(), int(f.readline().strip()), int(f.readline().strip()), f.readline().strip())
                except ValueError:
                    break
                cnt += 1
        return cnt
    except FileNotFoundError:
        print("File is not found.")

def main():
    global arr
    ReadData()
    c = input("Enter color of frame: ")
    mw = int(input("Enter max width: "))
    mh = int(input("Enter max height: "))
    found = False
    for i in range(len(arr)):
        if arr[i] != None and arr[i].getWidth() == mw and arr[i].getHeight() == mh and arr[i].getFramesilColor().casefold() == c.casefold():
            found = True
            print(arr[i].getDescription())
    if not found: print("Picture not found.")

if __name__ == "__main__":
    main()
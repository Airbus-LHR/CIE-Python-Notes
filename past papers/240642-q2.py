class Node:
    def __init__(self, d):
        self.__LeftPointer = -1 #integer
        self.__Data = d #integer
        self.__RightPointer = -1 #integer
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    def SetLeft(self, l):
        self.__LeftPointer = l
    def SetRight(self, r):
        self.__RightPointer = r
    def SetData(self, d):
        self.__Data = d

class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1)] * 20 #array of type Nodes
        self.__FirstNode = -1 #integer
        self.__NumberNodes = 0 #integer
    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__FirstNode = 0
            self.__NumberNodes += 1
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            idx = self.__FirstNode
            while True:
                if self.__Tree[idx].GetData() > NewNode.GetData():
                    if self.__Tree[idx].GetLeft() == -1:
                        self.__Tree[idx].SetLeft(self.__NumberNodes)
                        break
                    else:
                        idx = self.__Tree[idx].GetLeft()
                elif self.__Tree[idx].GetData() < NewNode.GetData():
                    if self.__Tree[idx].GetRight() == -1:
                        self.__Tree[idx].SetRight(self.__NumberNodes)
                        break
                    else:
                        idx = self.__Tree[idx].GetRight()
            self.__NumberNodes += 1
    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(self.__NumberNodes):
                print(f"{self.__Tree[i].GetLeft()} {self.__Tree[i].GetData()} {self.__Tree[i].GetRight()}")

def main():
    TheTree = TreeClass()
    TheTree.InsertNode(Node(10))
    TheTree.InsertNode(Node(11))
    TheTree.InsertNode(Node(5))
    TheTree.InsertNode(Node(1))
    TheTree.InsertNode(Node(20))
    TheTree.InsertNode(Node(7))
    TheTree.InsertNode(Node(15))
    TheTree.OutputTree()

if __name__ == "__main__":
    main()
class Node:
    def __init__(self, n):
        self.__Nodedata = n #integer
        self.__LeftNode = None #object Node
        self.__RightNode = None #object Node
    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode
    def GetData(self):
        return self.__Nodedata
    def SetLeft(self, a):
        self.__LeftNode = a
    def SetRight(self, a):
        self.__RightNode = a

class Tree:
    def __init__(self, f):
        self.__FirstNode = f #object Node
    def GetRootNode(self):
        return self.__FirstNode
    def Insert(self, data):
        current = self.GetRootNode()
        while True:
            if data.GetData() >= current.GetData():
                if current.GetRight() != None:
                    current = current.GetRight()
                else:
                    current.SetRight(data)
                    break
            else:
                if current.GetLeft() != None:
                    current = current.GetLeft()
                else:
                    current.SetLeft(data)
                    break
    def OutputInOrder(self, n):
        if n.GetLeft() != None:
            self.OutputInOrder(n.GetLeft())
        print(n.GetData())
        if n.GetRight() != None:
            self.OutputInOrder(n.GetRight())

def main():
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(5)
    n4 = Node(15)
    n5 = Node(7)
    a = Tree(n1)
    a.Insert(n2)
    a.Insert(n3)
    a.Insert(n4)
    a.Insert(n5)
    a.OutputInOrder(a.GetRootNode())
if __name__ == "__main__":
    main()
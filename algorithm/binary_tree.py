class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

n = None
inp = 0
root = None
def insert(n, current):
    if n.num == current.num:
        return
    elif n.num < current.num:
        if current.left == None:
            current.left = n
        else:
            insert(n, current.left)
    elif n.num > current.num:
        if current.right == None:
            current.right = n
        else:
            insert(n, current.right)

def find(f, current):
    if current == None:
        return False
    elif f == current.num:
        return True
    elif f < current.num:
        return find(f, current.left)
    else:
        return find(f, current.right)

def iterate(current):
    if current != None:
        print(current.num)
        iterate(current.left)
        iterate(current.right)
    else: return

def main():
    global root
    flag = 0
    while True:
        flag += 1
        inp = int(input("Enter a number: "))
        if inp == -1:
            break
        n = Node(inp)
        if flag == 1:
            root = n
        insert(n, root)
    if find(int(input("Find an item: ")), root):
        print("Item found")
    else:
        print("Item not found")
    iterate(root)

if __name__ == "__main__":
    main()
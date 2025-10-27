class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
last = Node(None)
start = Node(None)
n = 0
flag = 0
def append(n):
    global last, start, flag
    t = Node(n)
    last.next = t
    last = t
    if flag == 1:
        start = last

def insert(n, pos):
    global start
    t = Node(n)
    it = start
    for i in range(pos - 1):
        if it is None:
            print("Position out of range.")
            return
        it = it.next
    if it is None:
        print("Position out of range.")
        return
    t.next = it.next
    it.next = t

def delete(n):
    global start
    it = start
    while it.next != None and it.next.num != n:
        it = it.next
    if it.next != None:
        it.next = it.next.next
    else:
        print("Item not found.")

def find(f):
    global start
    it = start
    while it.next != None and it.num != f:
        it = it.next
    if it.num == f:
        return True
    else:
        return False

def iterate():
    global start
    it = start
    while it != None:
        print(it.num)
        it = it.next

def main():
    global n, flag
    while True:
        flag += 1
        n = int(input("Enter a number: "))
        if n == -1:
            break
        append(n)
    if find(int(input("Find an item: "))):
        print("Item found")
    else: print("Item not found")
    insert(int(input("Insert an item: ")), int(input("Position: ")))
    iterate()

if __name__ == "__main__":
    main()
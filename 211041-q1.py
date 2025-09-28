def Unknown(x, y):
    if x < y:
        print(x + y)
        return Unknown(x + 1, y) * 2
    elif x == y:
        return 1
    else:
        print(x + y)
        return Unknown(x - 1, y) // 2

def IterativeUnknown(x, y):
    cnt = 1
    while x < y:
        print(x + y)
        x += 1
        cnt *= 2
    while x > y:
        print(x + y)
        x -= 1
        cnt //= 2
    return cnt

def main():
    print("Call of unknown:")
    print("x=10, y=15")
    print(Unknown(10, 15))
    print("x=10, y=10")
    print(Unknown(10, 10))
    print("x=15, y=10")
    print(Unknown(15, 10))
    print("Call of iterative unknown:")
    print("x=10, y=15")
    print(IterativeUnknown(10, 15))
    print("x=10, y=10")
    print(IterativeUnknown(10, 10))
    print("x=15, y=10")
    print(IterativeUnknown(15, 10))
    

if __name__ == "__main__":
    main()
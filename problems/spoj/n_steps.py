def print_num(x, y):
    if x == y:
        if x < 0:
            print("No Number")
        elif x % 2 == 0:
            print(x*2)
        else:
            print(2*(x-1)+1)
    elif x-y == 2:
        n = y+1
        if x < 2:
            print("No Number")
        elif n % 2 == 0:
            print(n*2 - 1)
        else:
            print(n*2)
    else:
        print("No Number")

def main():
    t = int(input())
    for i in range(t):
        x, y = input().split()
        x, y = int(x), int(y)
        print_num(x, y)

if __name__ == "__main__":
    main()
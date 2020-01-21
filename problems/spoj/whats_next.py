def main():
    while True:
        a,b,c = input().split()
        a,b,c = int(a), int(b), int(c)
        if a == 0 and b == 0 and c == 0:
            break
        if b*b == a*c:
            print("GP {}".format(int(c*c / b)))
        else:
            print("AP {}".format(int(2*c - b)))

if __name__ == "__main__":
    main()
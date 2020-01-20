def print_zeros(n):
    i = 1
    num_zeros = 0
    while 5**i<=n:
        num_zeros += int(n / 5**i)
        i+=1
    print(num_zeros)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print_zeros(n)

if __name__ == "__main__":
    main()
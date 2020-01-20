# I learnt that: Slicing in lists

def reverse(n):
    n_str = str(n)
    # a[start:stop:step] -> slice operator
    return int(n_str[::-1])

def main():
    t = int(input())

    for i in range(t):
        n, m = input().split()
        n, m = int(n), int(m)
        sum = reverse(reverse(n) + reverse(m))
        print(sum)

if __name__ == "__main__":
    main()
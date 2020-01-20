def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(factorial(n))

if __name__ == "__main__":
    main()
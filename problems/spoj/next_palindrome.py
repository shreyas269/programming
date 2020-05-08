def next_palindrome(s):
    s = str(int(s) + 1)
    s = list(s)
    l = len(s)
    m = (l-1) // 2
    right = (l + 1) // 2
    left = (l // 2) - 1
    num = s
    while left >= 0:
        if s[left] < s[right]:
            num = list(str(int(''.join(s)) + 10 ** (l-1-m)))
            break

        elif s[left] > s[right]:
            break

        left-=1
        right+=1

    for i in range(len(num) // 2):
        num[-1 - i] = num[i]

    print(int(''.join(num)))

def main():
    t = int(input())
    for i in range(t):
        next_palindrome(input())

if __name__ == "__main__":
    main()

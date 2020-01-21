def print_digit(a,b):
    if (b==0):
        return 1
    ld = a % 10
    if ld==1 or ld==5 or ld==6 or ld==0:
        return ld
    elif ld==2:
        return (2**((b%4)+4))% 10
    elif ld==3:
        return (3**((b%4))) % 10
    elif ld==4:
        return (4**((b%2)+2))% 10
    elif ld==7:
        if(b==1):
            return 7
        else:
            return (7**((b%4)+4))% 10
    elif ld==8:
        return (8**((b%4)+4))% 10
    elif ld==9:
        return (9**(b%2))%10

def main():
    t =int(input())
    for i in range(t):
        a,b = input().split()
        a,b = int(a), int(b)
        print(print_digit(a,b))

if __name__ == "__main__":
    main()
def main():
    while True:
        n = int(input())
        if n == -1:
            break
        _list = []
        for i in range(n):
            _list.append(int(input()))
        if sum(_list) % n != 0:
            print(-1)
        else:
            avg = int(sum(_list) / n)
            cnt = 0
            for i in range(n):
                if _list[i] > avg:
                    cnt+= _list[i] - avg
            print(cnt)

if __name__ == "__main__":
    main()
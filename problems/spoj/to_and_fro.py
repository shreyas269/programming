# I learnt that: Work out the formula on paper completely and then only start coding

def main():
    while True:
        c = int(input())
        if c == 0:
            break
        s = input()
        r = int(len(s)/c)
        _output = ""
        for i in range(c):
            cnt = 0
            idx = i
            _output += s[idx]
            cnt += 1
            while cnt < r:
                if cnt >= r:
                    break
                idx += 2*(c-i)-1
                _output += s[idx]
                cnt += 1
                if cnt >= r:
                    break
                idx += 2*(i+1)-1
                _output += s[idx]
                cnt += 1
        print(_output)

if __name__ == "__main__":
    main()
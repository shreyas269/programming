# I learnt that: Look for all edge cases before coding the solution
def main():
    while True:
        s = input()
        if s  == '0':
            return

        n = len(s)

        dp = [-1] * n
        dp[0] = 1

        for i in range(1,n):
            if s[i] == '0':
                if i-2 < 0:
                    dp[i] = 1
                else:
                    dp[i] = dp[i-2]
            elif '10' <= s[i-1:i+1] <= '26':
                if i-2 < 0:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        print(dp[-1])


if __name__ == "__main__":
    main()
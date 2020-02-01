# I learnt that: Make constraint optimization later when you the solution correct
# and not at the beginning
def is_possible(stalls, num, C):
    possible = True
    count = 1  # Keeping a cow at the first stall
    left = 0
    for i in range(1, len(stalls)):
        right = i
        if (stalls[right] - stalls[left] >= num):
            count += 1
            left = right
        if count >= C:
            return True

    if count < C:
        return False

    return True


def main():
    t = int(input())
    # input-store
    for i in range(t):
        N, C = map(int, input().split())
        stalls = []
        for i in range(N):
            stalls.append(int(input()))

        stalls = sorted(stalls)

        # binary-search
        start = 1
        end = (stalls[-1] - stalls[0] + 1) // (C - 1)
        while (start < end):
            mid = start + (end - start + 1) // 2

            if is_possible(stalls, mid, C):
                start = mid
            else:
                end = mid - 1
        print(start)


if __name__ == "__main__":
    main()

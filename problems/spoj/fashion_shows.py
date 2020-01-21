# I learnt that: How to take list of integer input from line and convert to list
# list.sort(reverse = True) to sort it in descending order
# .sort needs to be called after the list is filled in or else you will get error
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        sum = 0
        men_list = [int(i) for i in input().split()]
        # call .sort only after the list is filled else it throws error in None type object
        men_list.sort(reverse = True)
        women_list = [int(j) for j in input().split()]
        women_list.sort(reverse = True)

        for i in range(n):
            sum+= men_list[i]*women_list[i]
        print(int(sum))

if __name__ == "__main__":
    main()
# I learnt that: First work out the algorithm completely in your mind and paper and then only start to code

from math import sqrt,ceil

primes = []

def seive(a, b):
    # create a list [True, True, ...] with indices [0,1,2,3.....,b]
    _list = [True for i in range(b+1)]
    p = 2
    # start with index 2 and cancel out all multiples of it starting from p*p with step size p
    while p*p <= b:
        if(_list[p] == True):
            for i in range(p*p, b+1, p):
                _list[i] = False
        p+=1

    for i in range(2, b):
        if _list[i] == True:
            primes.append(i)

def segmented_seive_spoj(l, r):
    if(l<2):
        l = 2

    # [True ...] block with indices [l, ..., r, ... 100000]
    _list = [True] * 100001
    _sqrt_r = int(sqrt(r))+1

    for p in primes:
        if p>_sqrt_r:
            break

        if p >= l:
            start = p*2
        else:
            # start = ceil(l/p) * p   #Bad way to write the same line below
            start = l + ( (p - l % p) % p)

        for i in range(start,r+1,p):
            _list[i-l] = False

    for i in range(l,r+1):
        if _list[i-l] == True:
            print(i, " ", end="")

def main():
    t = int(input())
    seive(1, int(sqrt(1000000000))+1)

    for i in range(t):
        a, b = input().split() # .split(<separator_char>)
        a, b = int(a), int(b)
        segmented_seive_spoj(a, b)
        if i < t:
            print()

if __name__ == "__main__":
    main()
from math import floor
from math import sqrt

def main():
    max_area = int(input())
    _output = 0
    max_bredth = floor(sqrt(max_area))
    for bredth in range(1,max_bredth+1):
        _output += ( floor(max_area/bredth) - (bredth-1) )
    print(_output)

if __name__ == "__main__":
    main()
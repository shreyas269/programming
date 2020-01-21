# DP question
# I learnt that: dp list need not be of very large size. A small subset of
# initial solutions would sometimes do. For the rest, program will call recursively.
#
# Exception Handling: input() will throw error at EOF if you are
# taking continuous inputs. Wrap input() in try except block
# or use stdin to take inputs

from sys import stdin
from math import floor

dp_list = [None]*int(100000) # check memory limits of the judge

def max_return(n):
    if(n < 10):
        return n
    if n < 100000:
        if dp_list[n] is not None:
            return dp_list[n]
        else:
            dp_list[n] = max(n, max_return(floor(n/2))+max_return(floor(n/3))+max_return(floor(n/4)))
            return dp_list[n]

    return max(n, max_return(floor(n/2))+max_return(floor(n/3))+max_return(floor(n/4)))

def main():
    # Two methods to read input for this problem
    # Prefer the second method
    method1 = False

    while method1:
        try:
            raw_input = input()
            if raw_input == '\n' or raw_input == '':
                break

            n = int(raw_input)
            value = max_return(n)
            print(value)
        except EOFError as error:
            break

    # Method to read input from stdin if we dont know how much
    # input is there
    for line in stdin:
        if line == '':  # If empty string is read then stop the loop
            break
        n = int(line.rstrip()) # removes all whitespaces from the end of line
        value = max_return(n)
        print(value)

if __name__ == "__main__":
    main()

# Determines the number of ways in which a given integer can be expressed as a sum of 1s, 2s, and 3s.  
# Input
# The input consists of T test cases. 
# The number of test cases (T ) is given in the first line of the input file.
# Each test case consists of an integer written in a single line.
# Output
# Print exactly one line for each test case. 
# For test

import sys

def calculation(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return calculation(n - 1) + calculation(n - 2) + calculation(n - 3)    

if __name__ == "__main__":
    N = sys.stdin.readline()
    inputs = [int(sys.stdin.readline()) for _ in range(int(N))]
    for n in inputs:
        print(calculation(n))
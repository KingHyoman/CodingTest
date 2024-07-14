# Program that calculates the highest sum of numbers passed on a route 
# that starts at the top and ends somewhere on the base.
### The number of rows in the triangle is ≥ 1 but ≤ 500 ###
# Input
# Data about the number of rows in the triangle are first read from the input.

import sys

def solution(inputs):
    results = [inputs[0]]
    for i in range(1, len(inputs)):
        n = len(inputs[i]) - 1
        result = []
        for j in range(len(inputs[i])):
            if j == 0 :
                maximum = results[i - 1][j] + inputs[i][j]
            elif j == n:
                maximum = results[i - 1][j - 1] + inputs[i][j]
            else:
                left = results[i - 1][j - 1] + inputs[i][j]
                right = results[i - 1][j] + inputs[i][j]
                maximum = max(left, right)
            result.append(maximum)
        results.append(result)
        
    return max(results[-1])

if __name__ == "__main__":
    N = sys.stdin.readline()
    inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(int(N))]
    print(solution(inputs))
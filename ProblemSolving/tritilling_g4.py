# In how many ways can you tile a 3xn rectangle with 2x1 dominoes?
# Given variable: n
# Return that an integer number giving the number of possible tilings.

import sys

def solution(n):
    front, back = 1, 3
    if n == 0 or n % 2 != 0:
        return 0
    else:
        for _ in range(1, n // 2):
            # The relation of n and n - 1
            new = back * 3 + front * 2
            front += back
            back = new
    
    return back

if __name__ == "__main__":
    N = sys.stdin.readline()
    print(solution(int(N)))
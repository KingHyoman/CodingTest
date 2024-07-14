# The Padovan sequence: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9 ...
# Let the Padovan sequence is P(T)
# If T is given(T is the positive integer), return the P(T)

# strategy: P(T) = P(T - 2) + P(T - 3)
# We can use DP, recursion in this problem
# But for the best time complexity => using the strategy

import sys

def solution(n):
    answer = 0
    back, middle, front = 1, 1, 1
    if n <= 3:
        return 1
    else:
        for _ in range(3, n):
            answer = back + middle
            back = middle
            middle = front
            front = answer
        return answer

if __name__ == "__main__":
    N = sys.stdin.readline()
    inputs = [int(sys.stdin.readline()) for _ in range(int(N))]
    for n in inputs:
        print(solution(n))
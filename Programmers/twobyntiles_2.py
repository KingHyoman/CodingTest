# There is a tile: 2 * 1
# We want to fill the given space using this tiles
# Given space: n * 2
# Find the num that all cases of filling the given space

# strategy
# Fibonacci
# There is a rule
# If space + 1, then the num of all cases increases following Fibonacci

def solution(n):
    answer = 0
    if n <= 3:
        return n
    stack = [2, 3]
    # For time complexity
    # using stack and pop() method
    for _ in range(4, n + 1):
        i = stack.pop()
        j = stack.pop()
        stack.append(i)
        stack.append(i + j)

    return stack[-1] % 1000000007

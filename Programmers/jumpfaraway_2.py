# Long jump
# H is a person who can jump 1 or 2 meter
# There is long jump which is n meter
# Figure out the cases of long jump
# given variable: n
# ex)
# n = 4
# (1, 1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 2)
# Thus the answer is 5

def solution(n):
    # This problem follows the fibonacci
    if n <= 2:
        return n
    else:
        n_1, n_0 = 1, 2
        for i in range(3, n + 1):
            new = n_1 + n_0
            n_1 = n_0
            n_0 = new
    return new % 1234567
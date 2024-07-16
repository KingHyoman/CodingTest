# Change below function more effectively
'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

# strategy
# Using dynamic programming to store the former step of function
# This function has 3 parameters -> we need to use 3-dimensional function
import sys

def w(a, b, c):
    # 3-dimension of list also can be declared
    check_list = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    if a <= 0 or b <= 0 or c <= 0:
        # case1: necessary
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        # case2: nesessary
        a = 20
        b = 20
        c = 20

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if i == 0 or j == 0 or k == 0:
                    check_list[i][j][k] = 1
                elif i < j and j < k:
                    check_list[i][j][k] = check_list[i][j][k - 1] + check_list[i][j-1][k-1] - \
                        check_list[i][j - 1][c]
                else:
                    check_list[i][j][k] = check_list[i - 1][j][k] + check_list[i - 1][j - 1][k] + \
                        check_list[i - 1][j][k - 1] - check_list[i - 1][j - 1][k - 1]
                    
    return check_list[i][j][k]

if __name__ == "__main__":
    # To get all parameters until (-1, -1, -1)
    parameters = []
    while True:
        a, b, c = list(map(int, sys.stdin.readline().split()))
        if a == -1 and b == -1 and c == -1:
            break
        parameters.append([a, b, c])

    # Execute all cases in parameters
    for inputs in parameters:
        print(f'w({inputs[0]}, {inputs[1]}, {inputs[2]}) = {w(inputs[0], inputs[1], inputs[2])}')
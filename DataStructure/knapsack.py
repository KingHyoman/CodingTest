# 0/1 Knapsack: until given weight limitation, make maximum profit
# input: n, m, p, w
# n: number of things(int)
# m: weight limitation(int)
# p: profits of each things(list of int)
# w: weight of each things(list of int)
# Strategy
# Using tabulation => make a matrix and fill all matrix

def knapSack(n, m, P, W):
    matrix = [[0 for i in range(m+1)] for j in range(n+1)]      # making matrix

    # visit all elements in matrix to upgrade the elements
    for j in range(n+1):
        for i in range(m+1):
            if i == 0 or j == 0:
                matrix[j][i] = 0
            elif i < W[j-1]:    # not if, should be elif
                matrix[j][i] = matrix[j-1][i]
            else:
                matrix[j][i] = max(P[j-1] + matrix[j-1][i-W[j-1]], matrix[j-1][i])
    print(matrix)
    
    return matrix[n][m]

P = [1,2,5,6]
W = [2,3,4,5]
m = 8
n = len(P)
print(knapSack(n, m, P, W))
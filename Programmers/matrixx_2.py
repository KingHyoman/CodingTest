# The product of matrix
# If two matrixs are given, return the product of matrix
# ex) arr1 = [[1, 4], [3, 2], [4, 1]], arr2 = [[1, 3], [3, 1]]
# then return [[13, 7], [9, 11], [7, 13]]

# if given array is m * r and r * n
# Then the result is m * n

def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2[0])
    mn = len(arr1[0])
    answer = []
    for j in range(m):
        answer_tem = []
        for i in range(n):
            tem = 0
            for k in range(mn):
                tem += arr1[j][k] * arr2[k][i]
            answer_tem.append(tem)
        answer.append(answer_tem)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[1, 3], [3, 1]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
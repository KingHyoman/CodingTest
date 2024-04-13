# figure out the biggest num using 'the common digit' from two nums
# ex) X = 3403, Y = 13203
# The common digits are 3, 0, 3
# Thus, the result is 330
# If there is no common digits then return -1


## using sort: O(n log n)
def solution_(X, Y):
    answer = ''
    X_list, Y_list = sorted([x for x in X]), sorted([y for y in Y])
    i, j = 0, 0
    while i < len(X_list) and j < len(Y_list):
        if X_list[i] == Y_list[j]:
            answer += str(X_list[i])
            i += 1
            j += 1
        elif X_list[i] > Y_list[j]:
            j += 1
        elif Y_list[j] > X_list[i]:
            i += 1
    if not answer:
        return '-1'
    if answer[len(answer) - 1] == '0':
        return '0'
    return answer[::-1]

## using python count: O(n)
def solution(X, Y):
    X_list , Y_list = [X.count(str(x)) for x in range(10)], [Y.count(str(y)) for y in range(10)]
    answer = ''
    for i in range(10):
        tem = min(X_list[i], Y_list[i])
        answer += str(i) * tem
    if not answer:
        return '-1'
    if answer[len(answer) - 1] == '0':
        return '0'
    return answer[::-1]

print(solution("12321", "42531"))
# If an natural num n is given, then figure out the num of cases
# that sum of consecutive num
# ex) n = 15
# 1 + 2 + 3 + 4 + 5, 4 + 5 + 6, 7 + 8, 15
# The answer is 4
# n < 10000

# Strategy
# Find all cases(because n < 10000)
def solution(n):
    answer = 0
    for i in range(1, n):
        sum = i
        for j in range(i + 1, n):
            sum += j
            if sum > n:
                break
            elif sum == n:
                answer += 1
    return answer + 1
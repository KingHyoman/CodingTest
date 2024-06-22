# There is a tournament match which N(even num) people are matching
# 'A' participant wants to know which round will play with 'B' participant
# Assume that 'A' and 'B' are always winner
# Given: N, A, B
# N = 8, A = 4, B = 7

# First strategy
# They meet when the difference become 1
# Use quotient, thus -1
def solution_1(n,a,b):
    answer = 1
    a -= 1
    b -= 1
    while abs(a - b) > 1:
        a //= 2
        b //= 2
        answer += 1

    return answer

# First strategy has a problem
# ex) N=8, A=2, B=3
# A and B has difference 1, but they meet in next match
# Thus if A is not odd then +1
def solution_2(n,a,b):
    answer = 1
    a -= 1
    b -= 1
    while abs(a - b) > 1:
        a //= 2
        b //= 2
        answer += 1
    if a > b and b % 2 != 0 or a < b and a % 2 != 0:
        return answer + 1
    return answer

# Second strategy has a problem
# ex) N=8, A=4, B=5
# A and B meet in the final match(3) but return 2
# Basically, they meet when they become same number
def solution(n,a,b):
    answer = 1
    a -= 1
    b -= 1
    while abs(a - b) > 0:
        a //= 2
        b //= 2
        answer += 1
    return answer - 1
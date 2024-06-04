# There is a 124 country that uses only "1, 2, 4" in natural number
# For example: 1 -> 1, 2 -> 2, 3 -> 4, 4 -> 11, 5 -> 12
# 6 -> 14, 7 -> 21, 8 -> 22, 9 -> 24, 10 -> 41
# Change the decimal num into the num using "1, 2, 4" only

# strategy
# This country uses only 3 nums, thus it will have high relationship
# with base 3.
# (base 3) -> (1, 2, 4 nums)
# 1 -> 1, 2 -> 2, 10 -> 4, 11 -> 11, 12 -> 12, 20 -> 14, 21 -> 21
# 22 -> 22, 100 -> 24, 101 -> 41, 102 -> 42, 110 -> 44
# 111 -> 111, 112 -> 112, 120 -> 114 ...
# Almost same but there is a little bit difference
# The difference between two relationships is only 0 and 4

def solution(n):
    answer = ''
    while n > 0:
        # The case with 0(4 in 124 country)
        # There is a rule
        if n % 3 == 0:
            answer += '4'   # First add 4 instead of 0
            n = n // 3 - 1     # store n // 3 - 1 instead of n // 3
        # The case without 0(4 in 124 country)
        else:
            answer += str(n % 3)
            n //= 3

    
    return answer

print(solution(10))
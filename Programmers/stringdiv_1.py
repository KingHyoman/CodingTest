# Given variable: string s
# Assume that the first character of string is x
# Count that the num of x and the num of not x from left to right of string
# If the num of x and the num of not x become same, then stop and count
# Following the above rule, return the total count 

def solution(s):
    answer = 0
    idx_bit = 0
    that = 0
    not_that = 0

    for letter in s:
        if not idx_bit:
            first = letter
            idx_bit = 1
        if letter == first:
            that += 1

        else:
            not_that += 1

        if that == not_that:
            answer += 1
            idx_bit = 0
            that = 0
            not_that = 0

    if idx_bit:
        answer += 1

    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
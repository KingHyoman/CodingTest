# Given variable: s(string)
# 1. Find a pair of two identical letters placed consecutively
# 2. Eliminate the pair, then concatenate the split strings
# Repeat 1 and 2
# Return 1 if success, else 0

# strategy
# using stack
def solution(s):
    stack = []
    for letter in s:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    return 0 if stack else 1

print(solution("baabaa"))
print(solution("cdcd"))
# given variable: num(natural num), k(natural num)
# Ex) 1924 and k = 2
# Figure out the biggest num without k digits
# Then 94 is the answer

# First strategy: using combination
# Simple but bad timecomplexity
import itertools

def solution_(number, k):
    ## time over
    answer = 0
    results = list(map(''.join, itertools.combinations(number, len(number) - k)))
    for result in results:
        if int(result) > answer:
            answer = int(result)
    return str(answer)

# Second strategy: using two pointer
# also bad time complexity
def solution_2(number, k):
    ## time over
    i = 0
    j = len(number) - 1
    mid = k
    answer = ''
    while len(answer) != len(number) - k:
        max_int = 0
        for idx in range(i, mid + 1):
            if max_int < int(number[idx]):
                i = idx
                max_int = int(number[idx])
        answer += number[i]
        i += 1
        mid += 1
    return answer

# Final: using stack
# O(n)
def solution(number, k):
    stack = []

    # the pop() calculation repeat k times
    for i in range(len(number)):
        while stack and k > 0 and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
        stack.append(number[i])

    # refer the second test case
    return ''.join(stack[:len(number) - k])

print(solution("1231234", 3))
print(solution("99991", 3))
print(solution("111119", 3))
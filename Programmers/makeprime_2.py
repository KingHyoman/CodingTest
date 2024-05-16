# Given variable: numbers
# 'numbers' is string of natural num "12345" is an example of 'numbers'
# Each num means the cards of natural num
# For example, "123" means, there are three cards with 1, 2, and 3.
# Find the num of prime number among the nums from the combination of cards
# test case
# "17" => 1 and 7
# then, 1, 7, 17, 71
# 7, 17, 71 are prime num thus the answer is 3.

# strategy
# 1. make a function to detect it is prime number
# 2. make all permutations using itertools
# 3. using set to avoid same num
import itertools

def isprime(n):
    # strategy 1
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            # the best time complexity: using sqrt to find prime num
            if n % i == 0:
                return False
        return True

def solution(numbers):
    # using set to avoid same num
    result = set()
    for cnt in range(1, len(numbers) + 1):
        # make all permutations
        tem = list(map(''.join, itertools.permutations(numbers, cnt)))
        for num in tem:
            if isprime(int(num)):
                result.add(int(num))
    return len(result)


print(solution("17"))
print(solution("011"))

# input is n
# return the number of prime number until n
# if n = 10 -> 2, 3, 5, 7, thus 4 is returned

import math

def isPrime(n):
    pivot = int(math.sqrt(n))
    print(pivot)
    for i in range(2, pivot + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if isPrime(i):
            answer += 1
    return answer

print(isPrime(7))
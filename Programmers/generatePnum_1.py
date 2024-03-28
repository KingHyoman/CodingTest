# Given an array nums containing numbers as the parameter
# Select three nums in arr
# return the num of cases that generate P num among the selected nums
# ex) [1,2,3,4] -> 1
# reason: 7 can be generated when using [1,2,4]

import math

def isPrime(n):
    pivot = int(math.sqrt(n))
    for i in range(2, pivot + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]):
                    cnt += 1
    return cnt

## other solutions
## using python combination library
## to compare time complexity
from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):     # to select three nums
        s = sum(i)
        chk = True  # checking bit  
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:  # if not Pnum then break
                chk = False
                break
        if chk is True:
            answer += 1     # if Pnum then cnt
    return answer

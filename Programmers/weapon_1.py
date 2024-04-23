# The knight has their own num
# They can buy a weapon that has power until the num of cd of their own number
# If the num of cd is greater than limit, then they can buy only restricted power
# Given variable => number(number of knight), limit, power
# Test case
# num: 10, limit: 3, power: 2
# The num of CD until 10: [1, 2, 2, 3, 2, 4, 2, 4, 3, 4]
# limit is 3 thus the knight of 6, 8, 10 can buy weapon that has power 3

def numofCD(n):
    cnt = 0
    if n == 1:
        return 1
    if n == 2 or n == 3:
        return 2
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
    if n ** 0.5 == int(n ** 0.5):
        return cnt * 2 - 1
    return cnt * 2

def solution(number, limit, power):
    answer = 0
    tem = []
    for i in range(1, number + 1):
        num = numofCD(i)
        if num > limit:
            answer += power
        else:
            answer += num

    return answer


print(solution(10, 3, 2))
# Pocketmon
# N: the number of all Poketmons
# we can catch N/2
# Using hashing to represent the value of max poketmons we can catch

def solution(nums):
    new = []
    n = len(nums) // 2
    for i in nums:
        if i not in new:
            new.append(i)
    if len(new) > n:
        return n
    return len(new)

print(solution([3, 1, 2, 3]))
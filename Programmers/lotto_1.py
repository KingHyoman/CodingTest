# Lotto 6/45: popular lottery game where six numbers are drawn from a pool of 45 numbers
# There are 6 tiers
# 1 -> all six nums match, 2 -> five nums match ... 5 -> two nums match, 6 -> others
# You bought lotto but little brother drew scribbles, thus that you can't make out some of its numbers
# calculate the highest tier and lowest tier
# Test cases
# lotto: [44, 1, 0, 0, 31, 25], win_nums: [31, 10, 45, 1, 6, 19]
# '0' is the part that little brother drew scribbles
# lowest is 5 and highest is 3 thus return [3, 5]

def solution(lottos, win_nums):
    cnt = 0
    cnt_0 = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            cnt_0 += 1
    if cnt == 6:
        return [1, 1]
    if cnt_0 == 6:
        return [1, 6]
    if cnt == 0:
        return [6 - (cnt+cnt_0), 6 - cnt]
        pass

    return [7 - (cnt+cnt_0), 7 - cnt]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
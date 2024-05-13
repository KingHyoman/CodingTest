# Scoville scale: measurement of spicy
# There is a man who like spicy food
# He has crazy idea which makes all food's scoville scale
# upper than given K
# When he mix two foods, the scoville scale of mixed foods becomes the following formula
# mixed = the most unspicy one + the second unspicy one * 2
# Find out the minimun num of mixing
# ex) [1, 2, 3, 9, 10, 12], K = 7
# first, mix 1 and 2 then it becomes 5
# second mix 5 and 3 then it becomes 13
# Thus the answer is 2

import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)    # O(n)

    cnt = 0
    while scoville[0] < K:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        result = a + 2 * b
        hq.heappush(scoville, result)   # O(log n)
        cnt += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    

    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 1, 1, 1, 1], 100))
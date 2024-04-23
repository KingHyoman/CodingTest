# There is a TV program of singing competition
# Everyday, a singer is added in candidates
# Totally k singer can be candidates
# We want to figure out the lowest score among the candidates
# input: k, score
# k = 3, score = [10, 100, 20, 150, 1, 100, 200]
# [10] -> [10, 100] -> [10, 100, 20] -> [100, 20, 150] ->
# [100, 20, 150] -> [100, 150, 100] -> [150, 100, 200]
# thus the answer is [10, 10, 10, 20, 20, 100, 100]

import heapq as hq

def solution(k, score):
    answer = []
    h = []
    for i in score:
        if len(h) < k:
            hq.heappush(h, i)
            tem = hq.heappop(h)
            answer.append(tem)
            hq.heappush(h, tem)
        else:
            tem = hq.heappop(h)
            if i < tem:
                answer.append(tem)
                hq.heappush(h, tem)
            else:
                hq.heappush(h, i)
                tem = hq.heappop(h)
                answer.append(tem)
                hq.heappush(h, tem)
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
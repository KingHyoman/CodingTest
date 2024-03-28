# given variables => arr of demands, budget
# return the num of max that the maximum of dep can use
# ex) [1,3,2,5,4],	9 -> 3
# reason: 9 = 1 + 3 + 5 or 9 = 3 + 2 + 4

## time over
from itertools import combinations

def solution(d, budget):
    if sum(d) < budget:
        return len(d)
    for i in range(len(d), 1, -1):
        for j in combinations(d, i):
            if sum(j) == budget:
                return i
    if budget in d:
        return 1
    return 0
## time over


def solution(d, budget):
    d = sorted(d)   
    while sum(d) > budget:
        print(d)
        d.pop()
    return len(d)

print(solution([1,3,2,5,4], 3))
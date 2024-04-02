# There is a developer who makes a game
# There are N stages in this game
# An array of integer is given that contains about the users are playing in that stage
# This developer wants to calculate "failure ratio" of each stages and sort it by descending order of "failure ratio"
# Test Case
# N = 5, arr = [2, 1, 2, 6, 2, 4, 3, 3]
# 1st stage: 1/8, 2nd stage: 3/7, 3rd stage: 2/4, 4th stage: 1/2, 5th stage: 0/1
# if there are same value of "failure ratio", then smaller stage comes fast.

def solution(N, stages):
    # using dict
    answer = {}
    # count the people of each stages
    for i in range(1, N + 1):
        answer[i] = 0
    for num in stages:
        if num <= N:
            answer[num] += 1
    
    # sort the array to calculate "failure ratio" easier
    stages = sorted(stages)
    m = len(stages)
    for i in answer:
        tem = answer[i]
        if m != 0:
            answer[i] = answer[i] / m
        m -= tem
    # sort by condition
    answer = sorted(answer.items(), key=lambda x: (x[1], -x[0]))[::-1]

    return [i[0] for i in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
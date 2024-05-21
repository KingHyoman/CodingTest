# given variables: k, dungeons
# There is a game and k means full hp of the character
# 'dungeons' is the array of array, and this array contains two integer
# let [x, y]
# x means the minimun hp to enter this dungeon and y means decreasing hp
# end ot the dungeon
# The player wants to visit as possible as many dungeons in this game
# return the maximum value of visiting

import itertools

def solution(k, dungeons):
    answers = []
    # the orders of visiting
    cases = list(itertools.permutations([i for i in range(len(dungeons))], len(dungeons)))
    full = k

    # check all cases
    for case in cases:
        cnt = 0
        for i in case:
            if dungeons[i][0] > full:
                break
            else:
                full -= dungeons[i][1]
                cnt += 1
        answers.append(cnt)
        full = k
        
    return max(answers)

print(solution(80, [[80,20],[50,40],[30,10]]))

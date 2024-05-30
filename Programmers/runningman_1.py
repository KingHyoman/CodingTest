# There is a running competition
# Some runners are running in this competition, and the narrator says about it
# If a runner passes the other runner, the narrator call the runner who passed someone
# For example,
# "mumu", "soe", "poe" are running and the narrator call "soe"
# then "soe", "mumu", "poe"
# Given varible: players, callings
# players: the initial order of competition
# callings: the order of runners who are called by narrator

def solution(players, callings):
    # when I realized that it seems be solved with using dic
    # consider using two dic
    PtoNum = {}
    NumtoP = {}

    # init of dic
    for i in range(len(players)):
        NumtoP[i + 1] = players[i]
        PtoNum[players[i]] = i + 1
    
    # change the order of runners by calling
    # name -> num -> name ...
    for calling in callings:
        num = PtoNum[calling]
        front = NumtoP[num]
        back = NumtoP[num - 1]
        NumtoP[num] = NumtoP[num - 1]
        NumtoP[num - 1] = front
        PtoNum[front] -= 1
        PtoNum[back] += 1

    answer = [NumtoP[i] for i in NumtoP]
    return answer


print(solution(["mumu", "soe", "poe", "kai", "mine"], \
               ["kai", "kai", "mine", "mine"]))
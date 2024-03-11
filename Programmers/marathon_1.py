# A marathon
# given variable: participant(list), completion(list)
# there is only one person that do not completed
# return that person

def solution(participant, completion):
    par = {}
    for p in participant:
        par[p] = 0
    for p in participant:
        par[p] += 1
    for c in completion:
        if par[c]:
            par[c] -= 1
    for i in par:
        if par[i] == 1:
            return i

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
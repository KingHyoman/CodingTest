# In certain game, there is a skill called bandage
# The bandage recover the hp of characters x per second
# If the character meets the t second, then it get additional y hp.
# If the character is attacked by monster, then this skill stops
# Also, the time of bandage reset in 0
# In this game, we want to know the final hp after monster's attacks
# there are three variables
# bandage: [casting time, healting per second, additional healthing]
# ex) [2, 1, 3]
# health: full hp
# ex) 20
# attacks: [attack time, damage]
# ex) [[1, 15], [6, 2]]


def solution(bandage, health, attacks):
    answer = health
    idx_attack = 0
    stack = 0
    for i in range(attacks[len(attacks) - 1][0] + 1):
        stack += 1
        if attacks[idx_attack][0] == i:
            stack = 0
            answer -= attacks[idx_attack][1]
            idx_attack += 1
        else:
            if stack == bandage[0]:
                answer += (bandage[1] + bandage[2])
                stack = 0
            else:
                answer += bandage[1]
            
            if answer > health:
                answer = health
        if answer <= 0:
            return -1

    return answer
'''
print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
print(solution([2, 1, 3], 20, [[1, 15], [6, 2]]))
'''
print(solution([10,10,100], 10, [[1,15],[3,1]]))
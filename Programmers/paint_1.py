# In school, there is a wall length n meters
# There is a brush length m meters
# The wall is divided by n, so there are n parts of wall(each 1 meter)
# You have to paint some parts of the wall because it getting old
# The school want to save budget, thus figure out the minimun num of painting
# Given variable: n, m, section(the parts of wall that have to paint)
# Ex) n = 8, m = 4, section = [2, 3, 6]
# (2, 3, 4, 5), (5, 6, 7, 8) thus 2

def solution(n, m, section):
    answer = 1
    start = section[0]
    end = start + m
    for i in section:
        if i >= end:
            start = i
            end = start + m 
            answer += 1

    return answer
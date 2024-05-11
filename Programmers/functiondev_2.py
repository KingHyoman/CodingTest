# Inputs: progresses and speeds
# progresses: the array of progressed percentage of function
# speeds: the array of percentage per day 
# There is a programmer who maintain the program
# There are some functions in this program, and the number of functions is the len of  progresses
# The programmer should release the functions following the order of progresses
# It means, for example, the second function developed faster than the first one
# have to wait until the developing of first function
# ex) progresses: [93, 30, 55], speeds: [1, 30, 5]
# then first function releases after 7 days
# second function releases after 4 dats
# third one releases after 9 days
# thus you have to return [2, 1]

# bad time complexity
def _solution(progresses, speeds):
    answer = []
    idx = 0
    while idx < len(progresses):
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if idx == i and progresses[i] >= 100:
                cnt += 1
                idx += 1
        if cnt != 0:
            answer.append(cnt)
    return answer

# good time complexity: O(n)
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        tem = 100 - progresses[i]
        days.append(tem // speeds[i] if tem % speeds[i] == 0 else (tem // speeds[i]) + 1)

    first = days[0]
    cnt = 0
    for day in days:
        if first >= day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            first = day
    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([1, 1, 1, 1], [100, 50, 99, 100]))

# There are n students in classroom
# The thief steels student's sportswear 
# Some student have spare sportwear and they can lend their spare sportwear
# But only can lend the sportwear nearby student => num3 can lend num2 or num4
# given variable => n, lost, reserve

def solution(n, lost, reserve):
    new = [1 for _ in range(n)]
    for i in lost:
        new[i-1] -= 1
    for i in reserve:
        new[i-1] += 1
    for i in range(len(new)):
        if i - 1 >= 0 and new[i-1] == 0 and new[i] == 2:
            new[i-1] += 1
            new[i] -= 1
        if i + 1 < len(new) and new[i+1] == 0 and new[i] == 2:
            new[i+1] += 1
            new[i] -= 1
    return new

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [1, 3], [1, 3, 4]))
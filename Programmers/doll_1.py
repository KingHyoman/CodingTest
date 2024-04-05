# Claw machine game
# There is n*n claw machine in monitor graphics and there is a doll in 1*1
# You can enter 1~n to choose doll
# The highest doll is choosed in n*n claw machine
# Choosed dolls are stacked another space(infinite) and if there are same dolls, that two dolls disappear
# Calculate how many dolls disppeared
# Test case
# n*n claw machine: [0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1], entered num arr: [1,5,3,5,1,2,1,4]
# Then 4 -> 3 -> 1 -> 1 -> 3 -> 2 -> 4 are choosed
# 3, 3 and 1, 1 disappear thus, the answer is 4

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in board:
            if i[move - 1] != 0:
                if stack and stack[len(stack) - 1] == i[move - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(i[move - 1])
                i[move - 1] = 0
                break
        
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
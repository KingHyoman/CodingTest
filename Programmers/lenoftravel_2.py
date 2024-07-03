# A game have 4 commands to move the robot
# U(move upward by one space), D(move downward by one space)
# R(move rightward by one space), L(move leftward by one space)
# The initial point of robot is (0, 0) and the space is x,y coordinate
# which -5 <= x <= 5, -5 <= y <= 5
# Given variable: dirs(the string of 4 commands)
# Return the len of traversal(have 2 conditions)
# 1. the length of the spaces where the character moves for the first time
# 2. the command moving over the border of the coordinate plane is ignored
# ex) "ULURRDLLU"
# (0, 0) -> (1, 0) -> (1, -1) -> (2, -1) -> (2, 0) -> (2, 1) -> (1, 1) -> (1, 0) //
# -> (1, -1) -> (2, -1)
# The answer is 7 because of condition 1(8th and 9th are the second time to visit)


def solution(dirs):
    answer = 0
    init = [0, 0]       # To store the init coordinate and the formal coordinate
    visited = set()     # To store the movement of the robot
    delta = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}      # dict for easy to use coordinate
    for dir in dirs:
        direction = delta[dir]
        coor_x, coor_y= init[0] + direction[0], init[1] + direction[1]
        if abs(coor_x) > 5 or abs(coor_y) > 5:
            # If not bounded in coordinate, ignore
            continue
        move = (init[0], init[1], coor_x, coor_y)   # movement(formal_x, formal_y, now_x, now_y)
        if move in visited:
            # if passed, do not count it
            pass
        else:
            visited.add(move)
            reverse_move = (coor_x, coor_y, init[0], init[1])   # The movement are 2 from 2 points
            visited.add(reverse_move)
            answer += 1
        init[0], init[1] = coor_x, coor_y
    return answer

print(solution("ULURRDLLU"))
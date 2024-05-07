# There is a 2D grid board where each cell is colored with a certain color.
# Given a cell, you want to find the number of adjacent cells 
# (up, down, left, and right) that have the same color.

def solution(board, h, w):
    answer = 0
    limit = len(board) - 1
    all_cases = [(h - 1, w), (h, w - 1), (h, w + 1), (h + 1, w)]
    for case in all_cases:
        if case[0] < 0 or case[1] < 0 or case[0] > limit or case[1] > limit:
            continue
        else:
            if board[h][w] == board[case[0]][case[1]]:
                answer += 1

    return answer

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
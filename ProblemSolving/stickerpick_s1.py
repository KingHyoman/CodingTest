# There is a sheet of 2n stickers of rectangular shape that are arranged in 2 rows and n columns
# Each sticker has a score
# We want to choose the stickers that becomes maximum score
# We cannot choose simultaneously thtat the two stickers share an edge
# Find the best score of the stickers

import sys

# Memory over(<128MB)
# Because of len(all_cases)
# The max len of inputs: 100,000
def solution_(sticker):
    all_cases = [[sticker[0][0], sticker[1][0]]]
    column = 0
    while column < len(sticker[0]) - 1:
        if len(sticker[0]) - column == 2:
            case1 = sticker[1][column + 1]
            case2 = sticker[0][column + 1]
            for i in range(len(all_cases[0])):
                if i % 2 != 0:
                    tem.append(all_cases[0][i] + case1)
                else:
                    tem.append(all_cases[0][i] + case2)

        else:
            case1 = sticker[1][column + 1] + sticker[0][column + 2]
            case2 = sticker[1][column + 2]
            case3 = sticker[0][column + 2]
            case4 = sticker[0][column + 1] + sticker[1][column + 2]
            tem = []
            for i in range(len(all_cases[0])):
                if i % 2 == 0:
                    tem.append(all_cases[0][i] + case1)
                    tem.append(all_cases[0][i] + case2)
                else:
                    tem.append(all_cases[0][i] + case3)
                    tem.append(all_cases[0][i] + case4)
        all_cases.pop()
        all_cases.append(tem)
        column += 2
    
    return max(all_cases[-1])

def solution(inputs):
    # The method that store all distance in given inputs
    # Because there are two cases of select path
    # idx - 1 or idx - 2
    
    # If the len of sticker is 1
    if len(inputs[0]) == 1:
        return max(inputs[0][0], inputs[1][0])
    
    inputs[0][1] += inputs[1][0]
    inputs[1][1] += inputs[0][0]
    idx = 1

    # If the len of sticker is greater than 3
    for idx in range(2, len(inputs[0])):
        inputs[0][idx] += max(inputs[1][idx - 1], inputs[1][idx - 2])
        inputs[1][idx] += max(inputs[0][idx - 1], inputs[0][idx - 2])

    return max(inputs[1][idx], inputs[0][idx])

if __name__ == "__main__":
    inputs = []
    N = sys.stdin.readline()
    for _ in range(int(N)):
        tem = sys.stdin.readline()
        inputs.append([list(map(int, sys.stdin.readline().split())) for _ in range(2)])
    for sticker in inputs:
        print(solution(sticker))

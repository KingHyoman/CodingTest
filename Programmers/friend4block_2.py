# There are m * n blocks game
# There are some characters in this game, and they are filled in blocks
# If the same characters are in 2 * 2, they disappear
# The upper characters are falling down into disappeared place
# Find how many blocks are disappeared

def solution(m, n, board):
    answer = 0
    condition = True
    new_board = [[board[i][j] for j in range(n)] for i in range(m)]

    while condition:
        # for the x, y coordinates 
        coor = set()
        coor_y = set()

        # Find the same characters in 2 * 2
        for i in range(m - 1):
            for j in range(n - 1):
                if new_board[i][j] != ' ' and \
                    new_board[i][j] == new_board[i + 1][j] and \
                        new_board[i][j] == new_board[i][j + 1] and \
                            new_board[i][j] == new_board[i + 1][j + 1]:
                    coor.update([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
                    coor_y.update([j, j + 1])

        # pang
        for x, y in coor:
            new_board[x][y] = " "

        # gravity code
        for y_coor in coor_y:
            x_coor = m - 1
            while x_coor > 0:
                if new_board[x_coor][y_coor] == ' ':
                    x_tem = x_coor
                    while x_coor > 0 and new_board[x_coor][y_coor] == ' ':
                        x_coor -= 1
                    if x_coor == 0 and new_board[x_coor][y_coor] == ' ':
                        break
                    else:
                        new_board[x_tem][y_coor] = new_board[x_coor][y_coor]
                        new_board[x_coor][y_coor] = ' '
                        x_coor = x_tem
                    
                x_coor -= 1
            
        # until there is no 2 * 2    
        if len(coor) == 0:
            break
        answer += len(coor)
    
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

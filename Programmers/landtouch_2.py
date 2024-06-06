# Suppose that you are going to play a hopscotch game
# The land is n * 4
# When moving down the rows one by one, stepping on the spaces, 
# you should only touch 1 space among the 4 spaces in the row.
# Special rule: the spaces on the same column cannot be touched consecutively
# Given variable: land(n * 4 array)
# Ex) land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]] 
# 5 -> 7(cannot touch 8) -> 4, thus 16

# First strategy
# Using integer variable to store the index of visited
def solution_(land):
    answer = 0
    visited = -1    # store the visited index
    for i in range(len(land)):
        maximum = 0
        for j in range(len(land[i])):
            # check if the index is visited in i - 1
            if land[i][j] > maximum and j != visited:
                visited = j
                maximum = land[i][j]
        answer += maximum
        
    return answer
# The problem:
# If there are same num in the land, then it cannot figure out the maximum value
# Counter Ex) land = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]

# Second strategy
# Using DP
# Store the best cases
def solution(land):
    visit_list = [land[0]]      # list to store the maximum store
    for i in range(1, len(land)):
        tem = []
        for j in range(len(land[0])):
            index = [num for num in range(4) if num != j]   # except the visited index in i - 1
            # Find the maximum value among the index
            maximum = max(visit_list[i - 1][index[0]] + land[i][j], \
                          visit_list[i - 1][index[1]] + land[i][j], \
                            visit_list[i - 1][index[2]] + land[i][j],)
            tem.append(maximum)
        visit_list.append(tem)
                             
    return max(visit_list[len(visit_list) - 1])

print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
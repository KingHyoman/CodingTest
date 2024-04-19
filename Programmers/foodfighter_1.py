# There is an food fighting competition
# There is a rule that making order of foods
# The order of foods: From low kcal to high kcal
# two people compete: one is from left, the other from right
# Input: the list of integers
# each elements means the num of foods
# ex) [1, 3, 4, 6] -> 1 - 3, 2 - 4 and 3 - 6 (0 means water)
# the output is order of foods
# "1223330333221"

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        tem = food[i] // 2
        answer += (str(i) * tem)
    return answer + '0' + answer[::-1]

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
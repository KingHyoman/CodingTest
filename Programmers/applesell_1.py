# An apple seller
# Apple has the grade from 1 to k(k is the best apple)
# Put m apples in one box
# if the lowest price of apple in box is p(1<=p<=k), then 
# that box costs m * p
# you can sell only unit of box(cannot sell one apple)
# Test cases
# [1, 2, 3, 1, 2, 3, 1], k = 3, m = 4
# [3, 3, 2, 2] => 2 * 4
# Thus 8

def solution(k, m, score):
    answer = 0
    score = sorted(score)
    while m <= len(score):
        for i in range(m):
            tem = score.pop()
            if i == m - 1:
                answer += (tem * m)
            pass

    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
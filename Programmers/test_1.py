# There are 3 people give up math
# They select the answer as a regular rule
# A => 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# B => 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# C => 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# And there is the original answer in this test
# Given variable => answer(list)
# return that who get the highest score following the answer

## using modular operation
## A: 5, B: 8, C: 10
def solution(answers):
    cnt_A, cnt_B, cnt_C = 0, 0, 0
    answers_A = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    answers_B = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    answers_C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)
    i = 0
    for answer in answers:
        if answer == answers_A[i]:
            cnt_A += 1
        if answer == answers_B[i]:
            cnt_B += 1
        if answer == answers_C[i]:
            cnt_C += 1
        i += 1
    
    results_dic = {1: cnt_A, 2: cnt_B, 3: cnt_C}
    max_ = 0
    for i in results_dic:
        if results_dic[i] > max_:
            max_ = results_dic[i]
    results_list = []
    for i in results_dic:
        if results_dic[i] == max_:
            results_list.append(i)
    return results_list

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
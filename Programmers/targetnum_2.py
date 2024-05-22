# given variables: numbers, target
# Ex) numbers: [1, 1, 1, 1, 1], target: 3
# There are only two operations, + and -
# You have to return the num of all cases
# that using all nums in numbers with two operations
# For ex, you have to make 3 using [1, 1, 1, 1, 1] with + and - operations
# -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, +1+1-1+1+1 = 3, +1+1+1-1+1 = 3, +1+1+1+1-1 = 3
# So the answer is 5

def solution(numbers, target):
    # using tree structures
    answers = [0]
    parent = 0

    # time complexity: O(2^n)
    for i in range(len(numbers)):
        for j in range(2 ** (i + 1)):
            if j % 2 == 0:
                answers.append(answers[parent] - numbers[i])
            elif j % 2 == 1:
                answers.append(answers[parent] + numbers[i])
                parent += 1
    
    # checking is it target
    cnt = 0
    for i in range(len(answers) // 2, len(answers)):
        if answers[i] == target:
            cnt += 1

    return cnt
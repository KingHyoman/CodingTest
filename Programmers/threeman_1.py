# There are students and they have their own num
# If sum of three students are 0 then they are called "samcyongsa"
# Given variable: list of num 
# Return the num of all cases of "samcyongsa"

def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
                pass
    return answer
# Like MBTI, there are 4 types of standards
# By survey, the personality is decided
# The total num of personality is 16 because 4 types of standards have 2 personality each on
# The each question in survey has 7 scores that decide the personality
# Return the result

def solution(survey, choices):
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] >= 5:
            score[survey[i][1]] += (choices[i] - 4)
        elif choices[i] <= 3:
            score[survey[i][0]] += (4 - choices[i])

    answer = ''
    cnt = 0
    for i in score:
        if cnt % 2 == 0:
            tem = i
        else:
            if score[i] > score[tem]:
                answer += i
            elif score[i] < score[tem]:
                answer += tem
            else:
                answer += min(i, tem)
        cnt += 1
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))

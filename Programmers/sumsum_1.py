# There are two arr are given
# return all cases of sum in one arr in ascending order

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
            
    return sorted(answer)
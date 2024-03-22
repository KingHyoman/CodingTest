# arr, divisor are given
# return sorted array that divide by divisor

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        return [-1]
    return sorted(answer)
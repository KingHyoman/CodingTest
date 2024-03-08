# Remove all duplicate nums in arr
# ex) [1, 1, 3, 3, 0 , 0, 1, 1] -> [1, 3, 0, 1] 

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])
        pass
    return answer

print(solution([1, 1, 3, 3, 0 , 0, 1, 1]))
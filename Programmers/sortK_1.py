# given variable => arr, i, j, k
# slice the arr from i to j
# ex) [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5 then, new array is [5, 2, 6, 3]
# Then select kth num from new sorted arr

def solution(array, commands):
    answer = []
    for idx in commands:
        i, j, n = idx[0], idx[1], idx[2]
        new_arr = array[i-1:j]
        new_arr = sorted(new_arr)
        answer.append(new_arr[n-1])
    return answer
# Find the max and min from given string
# ex) "1 2 3 4 5"
# return "1 5"
#

def solution(s):
    tem = ''
    arr = []
    for ch in s:
        if ch != ' ':
            tem += ch
        else:
            arr.append(int(tem))
            tem = ''
    arr.append(int(tem))
    return f'{min(arr)} {max(arr)}'

print(solution("-1 -1"))
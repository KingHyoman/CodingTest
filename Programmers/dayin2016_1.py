# a b 2016
# What day is it on a/b?

def solution(a, b):
    answer = {0: "THU", 1: "FRI", 2: "SAT", \
              3: "SUN", 4: "MON", 5: "TUE", 6: "WED"}
    ans = -1
    if a == 1:
        ans = b % 7
    elif a == 2:
        ans = (b + 31) % 7
    elif a == 3:
        ans = (b + 31 + 29) % 7
    elif a == 4:
        ans = (b + 31 + 29 + 31) % 7
    elif a == 5:
        ans = (b + 31 + 29 + 31 + 30) % 7
    elif a == 6:
        ans = (b + 31 + 29 + 31 + 30 + 31) % 7
    elif a == 7:
        ans = (b + 31 + 29 + 31 + 30 + 31 + 30) % 7
    elif a == 8:
        ans = (b + 31 + 29 + 31 + 30 + 31 + 30 + 31) % 7
    elif a == 9:
        ans = (b + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31) % 7
    elif a == 10:
        ans = (b + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30) % 7
    elif a == 11:
        ans = (b + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) % 7
    elif a == 12:
        ans = (b + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) % 7
    return answer[ans]
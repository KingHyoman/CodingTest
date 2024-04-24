# Given variable: two strings(t and p) that consist of integer
# len(t) >= len(p)
# if t = "3141592", p = "271"
# then first figure out all sub nums in t that have same length with p
# in this case: 314, 141, 415, 159, 592
# then count which is lower than p among above nums
# ans: 2

def solution(t, p):
    answer = 0
    n = len(p)
    i = 0
    while n < len(t) + 1:
        if int(t[i:n]) <= int(p):
            answer += 1
        i += 1
        n += 1
    return answer

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))